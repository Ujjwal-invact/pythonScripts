import pandas as pd

# Load CSV file
input_file = "./Alldata_with_singleemails.csv"  # Change this if needed
output_file = "./cleaned_data.csv"

# Read the CSV file
df = pd.read_csv(input_file)

# Remove rows where 'Email ID' is NaN or empty
if "Email ID" in df.columns:
    df = df[df["Email ID"].notna() & (df["Email ID"].str.strip() != "")]

# Save the cleaned file
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")
