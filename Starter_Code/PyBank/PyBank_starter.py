import os
import csv

# Construct the path to the CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Open the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header (optional, if your CSV has a header)
    header = next(csvreader)
    print(f"Header: {header}")

    # Loop through the rows in the CSV file and print them
    for row in csvreader:
        print(row)
