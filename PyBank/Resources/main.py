import os
import csv

# Construct the path to the CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Initialize counters and lists
total_months = 0
net_total = 0
previous_value = None  # To store the value of the previous row
changes = []  # To store month-to-month changes

# Open the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header (optional)
    header = next(csvreader)

    # Loop through the rows in the CSV file to count the months, sum column 2, and track changes
    for row in csvreader:
        total_months += 1
        current_value = int(row[1])  # Assuming values in column 2 are integers

        # Add the current value to the net total
        net_total += current_value

        # If there's a previous value, calculate the change and add to the changes list
        if previous_value is not None:
            change = current_value - previous_value
            changes.append(change)

        # Set the current value as the previous value for the next iteration
        previous_value = current_value

# Calculate the average change
if changes:  # Check to ensure we have changes to average
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

# Print the results
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: {average_change:.2f}")  # Printing to two decimal places
print("Greatest Increase in Profits:", max(changes))
print("Greatest Decrease in Profits:", min(changes))