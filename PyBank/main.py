import os
import csv

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
dates = []

# Read the CSV file
csvpath=os.path.join('.','Resources','budget_data.csv')
with open(csvpath) as file:
    csv_reader = csv.reader(file)
    csv_header = next(csv_reader)  # Skip the header row

    for row in csv_reader:
        # Extract date and profit/loss
        date = row[0]
        profit_loss = int(row[1])
        
        # Count total months
        total_months += 1
        
        # Calculate net total
        net_total += profit_loss
        
        # Calculate changes in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
        
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Find greatest increase in profits
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]

# Find greatest decrease in profits
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]
# Print the results
result = ("Financial Analysis\n"
"--------------------------------------------\n"
f"Total Months: {total_months}\n"
f"Net Total: ${net_total}\n"
f"Average Change: ${average_change:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Ensure the "analysis" directory exists
os.makedirs('analysis', exist_ok=True)

# Save the result to a text file in the "analysis" folder
#out_put = os.path.join('..',analysis','budget_data.txt')
with open('analysis/budget_data.txt', "w") as result_file:
   result_file.write(result)
   

   


print("Analysis results have been saved to 'analysis/budget_analysis.txt'.")