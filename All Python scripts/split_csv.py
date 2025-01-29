import pandas as pd
import os

# Input CSV file
input_file = "./fixed dates_2.csv"  # Ensure correct path
output_folder = "./split_csv_files"  # Folder to store smaller files
max_file_size_mb = 90  # Maximum file size in MB
max_file_size_bytes = max_file_size_mb * 1024 * 1024  # Convert MB to Bytes

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read CSV file in chunks (handling mixed types)
chunk_size = 100000  # Adjust chunk size if needed
df_iter = pd.read_csv(input_file, chunksize=chunk_size, dtype=str, low_memory=False)

# Splitting process
file_count = 1
current_chunk = pd.DataFrame()

for chunk in df_iter:
    current_chunk = pd.concat([current_chunk, chunk])  # Append new data to the existing chunk
    
    # Save when the file size exceeds the limit
    output_file = os.path.join(output_folder, f"split_part_{file_count}.csv")
    current_chunk.to_csv(output_file, index=False)

    if os.path.getsize(output_file) >= max_file_size_bytes:
        print(f"Saved {output_file} ({os.path.getsize(output_file) / (1024*1024):.2f} MB)")
        file_count += 1
        current_chunk = pd.DataFrame()  # Reset chunk for next file

# Save any remaining data
if not current_chunk.empty:
    output_file = os.path.join(output_folder, f"split_part_{file_count}.csv")
    current_chunk.to_csv(output_file, index=False)
    print(f"Saved {output_file} ({os.path.getsize(output_file) / (1024*1024):.2f} MB)")

print("CSV splitting complete!")
