import os
import zipfile
import shutil

def extract_and_collect_files(zip_folder, output_folder):
    """Extracts CSV and XLSX files from ZIP archives and moves them to a single folder."""
    
    temp_extract_folder = os.path.join(output_folder, "temp_extracted")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    if not os.path.exists(temp_extract_folder):
        os.makedirs(temp_extract_folder)
    
    seen_files = set()
    
    # Extract all ZIP files
    for zip_file in os.listdir(zip_folder):
        if zip_file.endswith('.zip'):
            zip_path = os.path.join(zip_folder, zip_file)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_extract_folder)

    # Collect all CSV and XLSX files
    for root, _, files in os.walk(temp_extract_folder):
        for file in files:
            if file.endswith('.csv') or file.endswith('.xlsx'):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(output_folder, file)
                
                # Avoid duplicates
                if file not in seen_files:
                    shutil.move(src_path, dest_path)
                    seen_files.add(file)

    # Remove the temporary extracted folder
    shutil.rmtree(temp_extract_folder)
    print(f"Extracted {len(seen_files)} unique files into {output_folder}")

# Set paths
zip_folder = "./files/Zips"
output_folder = "./files/Zips_combined"

# Run the extraction and file collection
extract_and_collect_files(zip_folder, output_folder)

