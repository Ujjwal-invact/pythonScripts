import pandas as pd

# Load CSV file
input_file = "./cleaned_data.csv"  # Change this if needed
output_file = "./cleaned_data_2.csv"

# Read the CSV file
df = pd.read_csv(input_file)

# Remove rows where 'Date of application' is NaN or empty
if "Date of application" in df.columns:
    df = df[df["Date of application"].notna() & (df["Date of application"].str.strip() != "")]

# Save the cleaned file
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")
