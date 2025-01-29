import pandas as pd
import os

# Input & output file paths
input_file = "./final_merged_data.csv"  # Change if needed
output_file = "./countfile.csv"
split_output_folder = "./new_split_csv_files"
split_required = False  # Change to False if splitting is not needed

# Required column names
required_columns = {
    "Job Title": "job_title",
    "Date of application": "date_of_application",
    "Name": "name",
    "Email ID": "email_id",
    "Phone Number": "phone_number",
    "Current Location": "current_location",
    "Preferred Locations": "preferred_locations",
    "Total Experience": "total_experience",
    "Curr. Company name": "curr_company_name",
    "Curr. Company Designation": "curr_company_designation",
    "Department": "department",
    "Role": "role",
    "Industry": "industry",
    "Key Skills": "key_skills",
    "Annual Salary": "annual_salary",
    "Notice period/ Availability to join": "notice_period",
    "Resume Headline": "resume_headline",
    "Summary": "summary",
    "Under Graduation degree": "ug_degree",
    "UG Specialization": "ug_specialization",
    "UG University/institute Name": "ug_university",
    "UG Graduation year": "ug_graduation_year",
    "Post graduation degree": "pg_degree",
    "PG specialization": "pg_specialization",
    "PG university/institute name": "pg_university",
    "PG graduation year": "pg_graduation_year",
    "Doctorate degree": "doctorate_degree",
    "Doctorate specialization": "doctorate_specialization",
    "Doctorate university/institute name": "doctorate_university",
    "Doctorate graduation year": "doctorate_graduation_year",
    "Gender": "gender",
    "Marital Status": "marital_status",
    "Home Town/City": "home_town",
    "Pin Code": "pin_code",
    "Work permit for USA": "work_permit_usa",
    "Date of Birth": "date_of_birth",
    "Permanent Address": "permanent_address"
}

# Year columns that need to be integers
year_columns = ["ug_graduation_year", "pg_graduation_year", "doctorate_graduation_year"]

# Date columns that need to be converted to YYYY-MM-DD
date_columns = ["date_of_application", "date_of_birth"]

# Function to split and expand email/phone columns
def split_expand(df, column):
    """Splits a column with multiple values (comma-separated) and expands rows."""
    df[column] = df[column].astype(str).str.split(',')
    df = df.explode(column)
    return df

# Read CSV in chunks to handle large files efficiently
chunksize = 100000
processed_chunks = []

for chunk in pd.read_csv(input_file, chunksize=chunksize, dtype=str, low_memory=False):
    # Split & Expand Email & Phone Number
    if 'Email ID' in chunk.columns:
        chunk = split_expand(chunk, 'Email ID')

    if 'Phone Number' in chunk.columns:
        chunk = split_expand(chunk, 'Phone Number')

    # Trim whitespace from email column before processing
    if "Email ID" in chunk.columns:
        chunk["Email ID"] = chunk["Email ID"].str.strip()

    # Keep only last 10 digits of phone numbers
    if "Phone Number" in chunk.columns:
        chunk["Phone Number"] = chunk["Phone Number"].astype(str).str[-10:]

    # Convert date columns to YYYY-MM-DD format
    for col in chunk.columns:
        if col in date_columns:
            chunk[col] = pd.to_datetime(chunk[col], errors="coerce").dt.strftime("%Y-%m-%d")
            chunk[col] = chunk[col].fillna("")  # Keep missing dates blank

    # Remove rows where Email ID is missing
    if "Email ID" in chunk.columns:
        chunk = chunk.dropna(subset=["Email ID"])  # Drop rows with NaN emails
        chunk = chunk[chunk["Email ID"] != ""]  # Drop rows with empty email strings
        chunk = chunk[chunk["Email ID"] != "nan"]  # Drop rows with empty email strings

    processed_chunks.append(chunk)

# Combine all processed chunks
df_cleaned = pd.concat(processed_chunks, ignore_index=True)

# Remove duplicate emails **AFTER processing**
if "Email ID" in df_cleaned.columns:
    initial_count = len(df_cleaned)
    df_cleaned = df_cleaned.drop_duplicates(subset=["Email ID"], keep="first")
    removed_count = initial_count - len(df_cleaned)
    print(f"\nTotal duplicate emails removed: {removed_count}")

# Rename columns
df_cleaned.rename(columns=required_columns, inplace=True)

# Convert year columns to integer
for col in year_columns:
    if col in df_cleaned.columns:
        df_cleaned[col] = df_cleaned[col].str.replace(".0", "", regex=False)
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce").astype("Int64")

# Convert date columns again (to be sure they remain in YYYY-MM-DD format)
for col in date_columns:
    if col in df_cleaned.columns:
        df_cleaned[col] = pd.to_datetime(df_cleaned[col], errors="coerce").dt.strftime("%Y-%m-%d")
        df_cleaned[col] = df_cleaned[col].fillna("")  # Keep missing dates blank

# Remove any extra columns
extra_columns = [col for col in df_cleaned.columns if col not in required_columns.values()]
if extra_columns:
    print("\nDeleting these extra columns:")
    for col in extra_columns:
        print(f"- {col}")
    df_cleaned = df_cleaned.drop(columns=extra_columns)

# Save the cleaned data
df_cleaned.to_csv(output_file, index=False)
print(f"\nCleaned data saved to {output_file}")

# # Optional: Split CSV into parts with 30,000 rows each
# if split_required:
#     os.makedirs(split_output_folder, exist_ok=True)

#     row_limit = 30000  # Set row limit per file
#     file_count = 1

#     for chunk in range(0, len(df_cleaned), row_limit):
#         output_file = os.path.join(split_output_folder, f"split_part_{file_count}.csv")
#         df_cleaned.iloc[chunk:chunk + row_limit].to_csv(output_file, index=False)
#         print(f"Saved {output_file} with {row_limit} rows")
#         file_count += 1

print("CSV splitting complete!")
