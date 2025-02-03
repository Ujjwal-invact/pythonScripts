# import os
# import pandas as pd

# # 📂 Folder containing Excel and CSV files to merge
# INPUT_FOLDER = "./files/zips_combined"  # Change this to your folder path

# # 📌 Output file path (CSV format)
# OUTPUT_FILE = "./testing_merge.csv"

# # 🚀 Function to merge all sheets from Excel and CSV files
# def merge_files_to_csv():
#     """Merges all sheets from Excel (.xlsx) and all CSV files from INPUT_FOLDER into a single CSV file."""
    
#     # Ensure the input folder exists
#     if not os.path.exists(INPUT_FOLDER):
#         print(f"❌ Error: Folder '{INPUT_FOLDER}' not found.")
#         return

#     # List all potential data files
#     files = [f for f in os.listdir(INPUT_FOLDER) if f.endswith((".xlsx", ".csv"))]

#     if not files:
#         print("❌ No Excel (.xlsx) or CSV files found in the folder.")
#         return

#     print(f"🔍 Found {len(files)} files. Merging...")

#     # Initialize an empty list to store dataframes
#     dataframes = []

#     for file in files:
#         file_path = os.path.join(INPUT_FOLDER, file)
#         print(f"📂 Reading file: {file}")

#         try:
#             if file.endswith(".xlsx"):
#                 # Read all sheets as dictionary of DataFrames
#                 sheets = pd.read_excel(file_path, dtype=str, engine="openpyxl", sheet_name=None)
                
#                 for sheet_name, df in sheets.items():
#                     print(f"   📄 Processing sheet: {sheet_name}")
#                     dataframes.append(df)

#             elif file.endswith(".csv"):
#                 df = pd.read_csv(file_path, dtype=str)
#                 dataframes.append(df)

#         except Exception as e:
#             print(f"❌ Error reading {file}: {e}")
#             continue  # Skip problematic files

#     # Merge all dataframes if any were read successfully
#     if dataframes:
#         merged_df = pd.concat(dataframes, ignore_index=True)

#         # Remove duplicate rows based on all columns (optional)
#         merged_df.drop_duplicates(inplace=True)

#         # Save merged file as CSV
#         merged_df.to_csv(OUTPUT_FILE, index=False)

#         print(f"✅ Merged {len(dataframes)} datasets successfully! Output saved to: {OUTPUT_FILE}")
#     else:
#         print("❌ No valid data files were merged.")

# # Run the merge function
# merge_files_to_csv()





# Run the function
# count_rows_and_duplicates(FILE_PATH)


# import pandas as pd

# # Input file path
# input_file = "./testing_Merge.csv"  # Change as needed

# # Read the CSV file
# df = pd.read_csv(input_file, dtype=str, low_memory=False)

# # Check if 'email_id' column exists
# if "email_id" in df.columns:
#     # Count duplicate occurrences
#     duplicate_counts = df["email_id"].value_counts()
    
#     # Filter only emails that appear more than once
#     duplicate_emails = duplicate_counts[duplicate_counts > 1]
    
#     # Print summary
#     print(f"Total duplicate emails: {duplicate_emails.count()}")
#     print("\nList of duplicate emails with counts:")
#     print(duplicate_emails)

#     # Save duplicate emails to a CSV file
#     duplicate_emails.to_csv("duplicate_emails_count.csv", header=["count"])
#     print("\nDuplicate emails saved to 'duplicate_emails_count.csv'")

# else:
#     print("Column 'email_id' not found in the dataset.")



import pandas as pd

# Input file path
input_file = "./outputs/processed_merged_output_2.csv"  # Change as needed

# Read the CSV file
df = pd.read_csv(input_file, dtype=str, low_memory=False)

# Count total number of rows
total_rows = len(df)
print(f"Total number of rows: {total_rows}")

# Count exact duplicate rows
exact_duplicate_rows = df.duplicated().sum()
print(f"Total number of exact duplicate rows: {exact_duplicate_rows}")

# Check if 'email_id' column exists
if "email_id" in df.columns:
    # Clean email_id column
    df["email_id"] = df["email_id"].str.strip().str.lower()  # Remove spaces & lowercase
    
    # Count unique email addresses
    unique_email_count = df["email_id"].nunique()
    print(f"Total unique emails: {unique_email_count}")

else:
    print("Column 'email_id' not found in the dataset.")
