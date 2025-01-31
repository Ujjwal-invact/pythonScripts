import pandas as pd

def count_csv_rows_pandas(file_path):
    return sum(1 for _ in open(file_path, 'r', encoding='utf-8')) - 1

csv_file_path = "./countfile.csv"
row_count = count_csv_rows_pandas(csv_file_path)
print(f"Total number of rows (excluding header): {row_count}")
