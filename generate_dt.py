import random
import sys
import re
import subprocess
import argparse
import os
from datetime import datetime, timedelta

# Check if the script is provided with the filename argument
if len(sys.argv) < 2:
    print("USAGE: python3 generate_dt.py --table_name tbl_name --dt_column_name dt_col_name --sample_size N")
    print("\t** tbl_name: name of the target table.")
    print("\t** dt_col_name: name of the datetime type column in the target table")
    print("\t** --sample-size=N : Sets the number of sample data (N) to be generated. If not specified, default value of 100 will be used")
    sys.exit(1)
elif len(sys.argv) > 7:
    print("ERROR: Too many arguments. USAGE: python3 generate_dt.py --table_name tbl_name --dt_column_name dt_col_name --sample_size N")
    sys.exit(1)

# Create ArgumentParser object
parser = argparse.ArgumentParser(description='Command-line argument parser')

# Parse command-line arguments
parser.add_argument('--sample_size', type=int, default=100, help='Sample size (default: 100)')
parser.add_argument('--table_name', type=str, required=True, help='Target table name')
parser.add_argument('--dt_column_name', type=str, required=True, help='Target datetime column name')

# Parse command-line arguments
args = parser.parse_args()

# Extract values from args
sample_size = args.sample_size
tgt_tbl_name = args.table_name
tgt_col_name = args.dt_column_name

# Function to generate random datetime within the same year
def random_datetime():
    start_date = datetime(year=2023, month=1, day=1)
    end_date = datetime(year=2024, month=2, day=26)
    delta = end_date - start_date
    random_date = start_date + timedelta(days=random.randint(0, delta.days))
    random_time = timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    return random_date.replace(hour=random_time.seconds // 3600, minute=(random_time.seconds % 3600) // 60, second=random_time.seconds % 60)

# Generate random datetime values
random_dt_list = [random_datetime() for _ in range(sample_size)]

# Sort the datetime values from oldest to newest
sorted_dt_list = sorted(random_dt_list)

# Get current date and time
current_datetime = datetime.now()
# Format current date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

# Append formatted date and time to output file name
output_file = f"{tgt_tbl_name}_{tgt_col_name}_{formatted_datetime}.sql"
mode = 'w'

#sql_insert_list = []
# Write SQL INSERT statements to the output file
with open(output_file, mode) as output:
      output.write(f'--Update statements generated for table {tgt_tbl_name} below:\n')
# Generate SQL INSERT statements for each random datetime value
      for i, random_dt in enumerate(sorted_dt_list, start=1):
          sql_update = f"UPDATE {tgt_tbl_name} SET {tgt_col_name} = '{random_dt.strftime('%Y-%m-%d %H:%M:%S')}' WHERE id = {i};"
          #sql_insert_list.append(sql_insert)
          output.write(sql_update + '\n')

print(f'output file generated: {output_file}')
print('file generated successfully...')
