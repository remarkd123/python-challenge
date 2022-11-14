# import dependencies
import os
import csv

# set file input path
budget_csv = os.path.join("Resources", "budget_data.csv")
# set file output path
analysis_out = os.path.join("Analysis", "financial_analysis.txt")

# lists to store data
# month tally to determine time range of data
budget_date = []
    
# Tracking profit/loss and monthly changes
budget_trans = []
delta_profit = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # read the header row
    header = next(csvreader)

    #iterate through each pair of values and add them to the empty lists 
    for row in csvreader:
        budget_date.append(row[0])
        budget_trans.append(int(row[1]))
    
    #iterate through all transactions and add them to the list of the delta(change) values
    for i in range(len(profit)-1):
        delta_profit.append(budget_trans[i+1]-budget_trans[i])

# evaluate the max and min from the list made
increase = max(delta_profit)
decrease = min(delta_profit)

# using the index function, determining the months of greatest increase and decrease
month_increase = delta_profit.index(max(delta_profit))+1
month_decrease = delta_profit.index(min(delta_profit))+1

with open(analysis_out,"w") as txt_file:
    # Standardizing output
    financial_analysis = (
       f"\nFinancial Analysis\n"
        f"------------------------\n"
        f"Total Months:  {len(budget_date)}\n"
        f"Total:  ${sum(budget_trans)}\n"
        f"Average Change:  ${round(sum(delta_profit)/len(delta_profit),2)}\n"
        f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})\n"
        f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})\n")

    print(financial_analysis)

    # Export the final vote count to the text file.
    txt_file.write(financial_analysis)