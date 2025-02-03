import os
import pandas as pd
import warnings

# Suppress warnings from openpyxl
warnings.simplefilter(action='ignore', category=UserWarning)

def merge_xlsx_files(input_folder, output_file, output_format="csv"):
    """Merges all .xlsx files (including multiple sheets) into one file."""
    
    all_data = []
    
    for file in os.listdir(input_folder):
        if file.startswith("._"):  # Skip macOS hidden system files
            print(f"Skipping macOS system file: {file}")
            continue

        if file.endswith('.xlsx') or file.endswith('.xls'):  # Handle both XLSX and XLS
            file_path = os.path.join(input_folder, file)
            
            try:
                engine = "openpyxl" if file.endswith('.xlsx') else "xlrd"
                xls = pd.ExcelFile(file_path, engine=engine)  # Specify engine manually
                
                for sheet_name in xls.sheet_names:
                    df = pd.read_excel(xls, sheet_name=sheet_name, engine=engine)
                    all_data.append(df)

            except ValueError as ve:
                print(f"Skipping {file} - Not a valid Excel file: {ve}")
            except Exception as e:
                print(f"Error processing {file}: {e}")  # Log error but continue

    # Merge all valid data
    if all_data:
        merged_df = pd.concat(all_data, ignore_index=True)

        # Save as CSV or XLSX
        if output_format.lower() == "csv":
            merged_df.to_csv(output_file, index=False)
        else:
            merged_df.to_excel(output_file, index=False, engine="openpyxl")

        print(f"✅ Successfully merged {len(all_data)} sheets into {output_file}")
    else:
        print("⚠️ No valid XLSX/XLS files found for merging.")

# # Set paths
# input_folder = "path/to/your/xlsx/files"  # Replace with your actual folder path
# output_file = "merged_output.csv"  # Change to .xlsx if needed

# # Run merging function
# merge_xlsx_files(input_folder, output_file, output_format="csv")  # Use "xlsx" for Excel output


# Set paths
input_folder = "./files/Zips_combined"  # Folder containing XLSX files
output_file = "merged_output_3.csv"  # Change to .xlsx if needed

# Run merging function
merge_xlsx_files(input_folder, output_file, output_format="csv")  # Use "xlsx" for Excel output