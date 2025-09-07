# Wealthsimple Statement Combiner

Wealthsimple allows you to download statements in CSV format, but only by month. Many people have a need for a single file with all transactions for the year so that they can do things like create pivot tables, manage their finances, and do taxes.

This is a script to combine all the CSV files in the current directory into a single CSV file.

## Instructions

1. **Clone this repo**
   ```bash
   git clone <repo-url>
   cd wealthsimple-combine-statements
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download all of your statements into this folder**
   - Download your monthly CSV statements from Wealthsimple
   - Place all CSV files in the same directory as the script

4. **Run the script**
   ```bash
   python combine.py
   ```

## Output

The script will:
- Show how many data rows are in each file
- Combine all files with a single header row
- Create `combined_statements.csv` with all your transactions
- Sort and organize the data properly

## Requirements

- Python 3.6+
- pandas