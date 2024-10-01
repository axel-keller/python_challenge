#import os/csv
import os
import csv
#define csv path
csvpath = os.path.join('', 'Resources', 'budget_data.csv')
file_to_output = os.path.join('', "analysis", "budget_analysis.txt")
#variables
total_months = 0
net_total = 0
previous = None
changes = []
months = []

# read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#header
    # Read the header
    header = next(csvreader)

    # Process each row in the CSV file
    for row in csvreader:
        total_months += 1
        current = int(row[1])

        net_total += current

        if previous is not None:
            change = current - previous
            changes.append(change)
            months.append(row[0])

        previous = current

# Calculate average change, greatest increase and greatest decrease
if changes:
    average_change = sum(changes) / len(changes)
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    greatest_increase_month = months[changes.index(greatest_increase)]
    greatest_decrease_month = months[changes.index(greatest_decrease)]
else:
    average_change = 0
    greatest_increase = greatest_decrease = 0
    greatest_increase_month = greatest_decrease_month = ""

# Print the results to the terminal
print("Financial Analysis")
print("--------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f"Average Change: ${average_change:.2f}")
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("--------------------------------\n")
    txt_file.write(f'Total Months: {total_months}\n')
    txt_file.write(f'Total: ${net_total}\n')
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    txt_file.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')
