

import pandas as pd
import numpy as np

# Input CSV file
input_file = "./new_upload.csv"  # Change if needed
output_file = "./cleaned_columns_12.csv"

# Define required columns
required_columns = [
    "job_title",
    "date_of_application",
    "name",
    "email_id",
    "phone_number",
    "current_location",
    "preferred_locations",
    "total_experience",
    "curr_company_name",
    "curr_company_designation",
    "department",
    "role",
    "industry",
    "key_skills",
    "annual_salary",
    "notice_period",
    "resume_headline",
    "summary",
    "ug_degree",
    "ug_specialization",
    "ug_university",
    "ug_graduation_year",
    "pg_degree",
    "pg_specialization",
    "pg_university",
    "pg_graduation_year",
    "doctorate_degree",
    "doctorate_specialization",
    "doctorate_university",
    "doctorate_graduation_year",
    "gender",
    "marital_status",
    "home_town",
    "pin_code",
    "work_permit_usa",
    "date_of_birth",
    "permanent_address"
]

# Read the CSV file
df = pd.read_csv(input_file, dtype=str)  # Read all as string to avoid conversion issues

# Find and delete extra columns
extra_columns = [col for col in df.columns if col not in required_columns]
if extra_columns:
    print("\nDeleting these extra columns:")
    for col in extra_columns:
        print(f"- {col}")

# Keep only required columns
df = df[[col for col in required_columns if col in df.columns]]

# Convert year columns to integers (remove ".0" issue)
year_columns = [
    "ug_graduation_year", "pg_graduation_year", "doctorate_graduation_year"
]
for col in year_columns:
    if col in df.columns:
        df[col] = df[col].str.replace(".0", "", regex=False)  # Remove ".0"
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")  # Convert to int, allow NULLs

# Save the cleaned file
df.to_csv(output_file, index=False)

print(f"\nCleaned data saved to {output_file}")
