import pandas as pd
import os

# Input & output file paths
input_file = "./final_merged_data.csv"  # Change if needed
output_file = "./cleaned_data.csv"
split_output_folder = "./New_new_split_csv_files"
split_required = True  # Change to True only if splitting is needed

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

    # Keep only last 10 digits of phone numbers
    if "Phone Number" in chunk.columns:
        chunk["Phone Number"] = chunk["Phone Number"].astype(str).str[-10:]

    # Convert all date columns to YYYY-MM-DD format
    for col in chunk.columns:
        if any(keyword in col.lower() for keyword in ["date_of_birth", "date_of_application"]):
            chunk[col] = pd.to_datetime(chunk[col], errors="coerce").dt.strftime("%Y-%m-%d")
            chunk[col] = chunk[col].fillna("")  # Keep missing dates blank

    # Remove rows where Email ID is NaN
    if "Email ID" in chunk.columns:
        chunk = chunk[chunk["Email ID"].notna() & (chunk["Email ID"].str.strip() != "")]

    # Remove rows where Date of Application is empty
    if "Date of application" in chunk.columns:
        chunk = chunk[chunk["Date of application"].notna() & (chunk["Date of application"].str.strip() != "")]

    processed_chunks.append(chunk)

# Combine all processed chunks
df_cleaned = pd.concat(processed_chunks, ignore_index=True)

# Rename columns
df_cleaned.rename(columns=required_columns, inplace=True)

# Remove any extra columns
extra_columns = [col for col in df_cleaned.columns if col not in required_columns.values()]
if extra_columns:
    print("\nDeleting these extra columns:")
    for col in extra_columns:
        print(f"- {col}")
    df_cleaned = df_cleaned.drop(columns=extra_columns)

# Convert year columns to integer
for col in year_columns:
    if col in df_cleaned.columns:
        df_cleaned[col] = df_cleaned[col].str.replace(".0", "", regex=False)
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors="coerce").astype("Int64")

# Save the cleaned data
df_cleaned.to_csv(output_file, index=False)
print(f"\nCleaned data saved to {output_file}")

# Optional: Split CSV into parts with 30,000 rows each
if split_required:
    os.makedirs(split_output_folder, exist_ok=True)

    row_limit = 30000  # Set row limit per file
    file_count = 1
    current_chunk = pd.DataFrame(columns=df_cleaned.columns)  # Ensure column structure

    for chunk in range(0, len(df_cleaned), row_limit):
        output_file = os.path.join(split_output_folder, f"split_part_{file_count}.csv")
        df_cleaned.iloc[chunk:chunk + row_limit].to_csv(output_file, index=False)
        print(f"Saved {output_file} with {row_limit} rows")
        file_count += 1

print("CSV splitting complete!")
