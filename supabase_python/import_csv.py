import os
import pandas as pd
from config import supabase  # Ensure config.py contains Supabase credentials

# Path to your CSV file
CSV_FILE_PATH = "../processed_old_merged_output.csv"

# Table name in Supabase
TABLE_NAME = "unique_email_applications"

# 🚀 Function to fetch all existing email IDs from the database
def get_existing_emails():
    """Fetch all existing email IDs from the database and ensure no duplicates."""
    existing_emails = set()
    
    # Pagination in case there are too many records
    limit = 10000  # Adjust if needed
    offset = 0

    while True:
        response = supabase.table(TABLE_NAME).select("email_id").range(offset, offset + limit - 1).execute()
        if not response.data:
            break  # Stop when no more data
        
        existing_emails.update(row["email_id"].strip().lower() for row in response.data if "email_id" in row)
        offset += limit

    return existing_emails

# 🚀 Function to load CSV and filter only missing emails
def find_missing_records():
    """Reads the CSV, compares emails with the database, and maps missing records."""
    
    # Load CSV
    df = pd.read_csv(CSV_FILE_PATH, dtype=str, low_memory=False)
    
    # Ensure column names are lowercase for consistency
    df.columns = df.columns.str.lower()

    # Check if 'email_id' exists in CSV
    if "email_id" not in df.columns:
        print("❌ Error: 'email_id' column not found in the CSV file.")
        return None

    # Fetch existing emails from the database
    existing_emails = get_existing_emails()

    # Standardize emails (lowercase + strip spaces) before filtering
    df["email_id"] = df["email_id"].astype(str).str.strip().str.lower()

    # Filter only new emails not in the database
    new_records = df[~df["email_id"].isin(existing_emails)]

    if new_records.empty:
        print("✅ No new records to insert.")
        return None
    
    print(f"✅ Found {len(new_records)} new records to insert.")
    
    # Convert NaN values to None (JSON-compliant format)
    new_records = new_records.where(pd.notnull(new_records), None)

    return new_records

# 🚀 Function to insert new records into Supabase using upsert
def insert_missing_records():
    """Insert missing records from CSV into Supabase, ignoring duplicates."""
    new_records = find_missing_records()

    if new_records is None:
        return

    # Convert dataframe to dictionary format for batch insertion
    records = new_records.to_dict(orient="records")

    # Insert records in batches to prevent rate-limiting
    batch_size = 50  # Adjust based on Supabase limits
    for i in range(0, len(records), batch_size):
        batch = records[i : i + batch_size]
        
        # Ensure batch is JSON-compatible
        batch = [{k: v if v is not pd.NA else None for k, v in row.items()} for row in batch]

        # Use UPSERT instead of INSERT to avoid duplicate key errors
        response = supabase.table(TABLE_NAME).upsert(batch, on_conflict=["email_id"]).execute()

        if response.data:
            print(f"✅ Successfully inserted {len(response.data)} new records in batch {i//batch_size + 1}.")
        else:
            print(f"⚠️ Error inserting batch {i//batch_size + 1}: {response.error}")

# Run the insert process
insert_missing_records()

