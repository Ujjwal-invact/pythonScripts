import pandas as pd

# Input file path
input_file = "./outputs/filtered_file2.csv"  # Change as needed
# output_file = "./outputs/cleaned_unique_rows.csv"  # Output file

# Read the CSV file
df = pd.read_csv(input_file, dtype=str, low_memory=False)

# Count total rows before removing duplicates
total_rows_before = len(df)
print(f"Total rows before removing duplicates: {total_rows_before}")

# # Remove exact duplicate rows and keep only one copy
# df_unique = df.drop_duplicates()

# # Count total rows after removing duplicates
# total_rows_after = len(df_unique)
# removed_rows = total_rows_before - total_rows_after
# print(f"Total exact duplicate rows removed: {removed_rows}")
# print(f"Total rows after removing duplicates: {total_rows_after}")

# # Save the cleaned file
# df_unique.to_csv(output_file, index=False)
# print(f"\nCleaned file saved to: {output_file}")




# import pandas as pd

# # Input file paths
# file1 = "./outputs/old_csv_outputs/new_merged_files_with_duplicates.csv"  # Reference file
# file2 = "./outputs/cleaned_unique_rows.csv"  # File to be checked
# output_file = "./outputs/filtered_file2.csv"  # File after removal

# # Flag to control whether to remove duplicates from file2
# remove_duplicates = False  # Set to True if you want to remove duplicates

# # Read both CSV files
# df1 = pd.read_csv(file1, dtype=str, low_memory=False)
# df2 = pd.read_csv(file2, dtype=str, low_memory=False)

# # Count total rows in file2 before comparison
# total_rows_file2 = len(df2)
# print(f"Total rows in file2 before checking: {total_rows_file2}")

# # Find exact duplicate rows in file2 that also exist in file1
# duplicate_rows = df2[df2.apply(tuple, axis=1).isin(df1.apply(tuple, axis=1))]

# # Count of duplicate rows
# duplicate_count = len(duplicate_rows)
# print(f"Total exact duplicate rows in file2 (matching file1): {duplicate_count}")

# # If remove_duplicates is False, stop here
# if not remove_duplicates:
#     print("Flag is set to False, so duplicate rows will not be removed.")
# else:
#     # Remove exact duplicates from file2
#     df2_cleaned = df2[~df2.apply(tuple, axis=1).isin(df1.apply(tuple, axis=1))]

#     # Count total rows in file2 after removal
#     total_rows_after = len(df2_cleaned)
#     removed_rows = total_rows_file2 - total_rows_after
#     print(f"Total exact duplicate rows removed: {removed_rows}")
#     print(f"Total rows in file2 after removing duplicates: {total_rows_after}")

#     # Save the cleaned file
#     df2_cleaned.to_csv(output_file, index=False)
#     print(f"\nFiltered file saved to: {output_file}")
