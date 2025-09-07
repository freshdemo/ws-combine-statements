import pandas as pd
import glob
import os

# Get all CSV files in the directory
csv_files = glob.glob("*.csv")

if not csv_files:
    print("No CSV files found in the current directory")
    exit()

print(f"Found {len(csv_files)} CSV files")

# Read and combine all files
dataframes = []
total_data_rows = 0

for i, file in enumerate(csv_files):
    df = pd.read_csv(file)
    data_rows = len(df)  # This counts data rows (header not included in len)
    total_data_rows += data_rows
    print(f"Reading {file}... {data_rows} data rows")
    dataframes.append(df)

# Concatenate all dataframes (this automatically handles the single header)
combined_df = pd.concat(dataframes, ignore_index=True)

print(f"\nSummary:")
print(f"Total data rows from all files: {total_data_rows}")
print(f"Combined dataframe has: {len(combined_df)} data rows")
print("Column names:", combined_df.columns.tolist())

# Save to new CSV with single header row
combined_df.to_csv('combined_statements.csv', index=False)
print(f"Saved to combined_statements.csv ({len(combined_df)} data rows + 1 header row)")