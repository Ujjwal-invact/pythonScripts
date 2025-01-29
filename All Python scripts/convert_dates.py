# import pandas as pd

# # Load CSV file
# input_file = "./cleaned_data_2.csv"  # Change this if needed
# output_file = "./fixed dates.csv"

# # Read the CSV file
# df = pd.read_csv(input_file, dtype=str)  # Read as string to avoid unwanted conversions

# # Function to identify date columns
# def is_date_column(column_name):
#     date_keywords = ["date", "dob", "application", "birth"]  # Common date-related words
#     return any(keyword in column_name.lower() for keyword in date_keywords)

# # Convert date columns to YYYY-MM-DD format
# for col in df.columns:
#     if is_date_column(col):
#         df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%Y-%m-%d")
#         df[col] = df[col].fillna("")  # Keep missing dates as blank

# # Save the cleaned file
# df.to_csv(output_file, index=False)
# print(f"Cleaned data saved to {output_file}")


import pandas as pd

# Load CSV file
input_file = "./cleaned_data_2.csv"  # Change this if needed
output_file = "./fixed dates_2.csv"

# Read the CSV file
df = pd.read_csv(input_file, dtype=str)  # Read as string to avoid unwanted conversions

# Function to identify date columns
def is_date_column(column_name):
    date_keywords = ["date", "dob", "application", "birth"]  # Common date-related words
    return any(keyword in column_name.lower() for keyword in date_keywords)

# Function to convert dates to YYYY-MM-DD format
def convert_date_column(series):
    for fmt in ("%d-%b-%y", "%d-%m-%Y", "%Y-%m-%d", "%m/%d/%Y"):  # Common formats
        try:
            return pd.to_datetime(series, format=fmt, errors="coerce").dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return pd.to_datetime(series, errors="coerce").dt.strftime("%Y-%m-%d")  # Fallback to default

# Convert date columns
for col in df.columns:
    if is_date_column(col):
        df[col] = convert_date_column(df[col])
        df[col] = df[col].fillna("")  # Keep missing dates as blank

# Save the cleaned file
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")
