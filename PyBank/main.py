# OS Module: This will will allow us to create paths across operating systems. 
import os

# CSV Module - Allows us to read csv files with python script. 
import csv

# File Path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Define lists to store data
Date = []
Net_Total = []
Profit = []
Total_Months = []
Change = []

# Initialize Variables
Profit_Start = 0
Month_Count = 0
Total_Profit = 0
Profit_Change = 0
Total_Change = 0

# Open as 
with open(csvpath) as csvfile:

    # CSV Reader
    csvreader = csv.reader(csvfile, delimiter=',')

    # CSV header
    csv_header = next(csvreader)

    # Commands for Each Row
    for row in csvreader: 

        # Append Column Headers
        Date.append(row[0])
        Profit.append(row[1])
        
        # Count the rows for the total number of months
        Month_Count = Month_Count + 1

        # Profit Total
        Total_Profit = Total_Profit + int(row[1])

        # Skip first row's monthly profit change
        if Month_Count == 1:
            nProfit = int(row[1])
            Profit_Start = nProfit

        # start on second months monthly profit change between month 1 and month 2
        # nProfit = Current Month profit/loss
        # Profit_Start = Previous Month profit/loss
        elif Month_Count != 1 and Month_Count != len(list(csvpath)):

            nProfit = int(row[1])
            Monthly_Profit_Change = nProfit - Profit_Start
            Change.append(int(Monthly_Profit_Change))
            Total_Change = Total_Change + Monthly_Profit_Change

            # Re-initialize Profit_Start as nProfit 
            Profit_Start = nProfit

        elif Month_Count == len(list(csvpath)):
            pass 
            
    # Average Change
    Average_Change = Total_Change / (Month_Count - 1)
    Average_Change = round(Average_Change, 2)

# Greatest Increase
Greatest_Increase = max(Change)

# Indexed Date for Greatest Increase
Increase_Date = Date[Change.index(Greatest_Increase)]

# Greatest Decrease 
Greatest_Decrease = min(Change)

# Indexed Date for Greatest Decrease
Decrease_Date = Date[Change.index(Greatest_Decrease)]

# Write Summary Table
print(" ")
print("Financial Analysis")
print("-------------------------------------")

# The total number of months included in the dataset
print("Total Months: ", str(int(Month_Count)))

# The net total amount of "Profit/Losses" over the entire period
print("Total: ", "$"+str(int(Total_Profit)))

# Format_Average = "{:.2f}".format(Average_Change)
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
print("Average Change: ", "$"+str("%.2f" % Average_Change))

# The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: ", Increase_Date, "($"+str(int(Greatest_Increase))+")")

# The greatest decrease in profits (date and amount) over the entire period
print("Greatest Increase in Profits: ", Decrease_Date, "($"+str(int(Greatest_Decrease))+")")

# Text Output
lines = ["Financial Analysis", "-------------------------------------", "Total Months: "+str(int(Month_Count)), "Total: "+"$"+str(int(Total_Profit)), "Average Change: "+"$"+str("%.2f" % Average_Change), "Greatest Increase in Profits: "+Increase_Date+" "+"($"+str(int(Greatest_Increase))+")", "Greatest Increase in Profits: "+Decrease_Date+" "+"($"+str(int(Greatest_Decrease))+")"]

# Output file
output = os.path.join("Analysis", "output.txt")

# Wrtie output as text file
with open(output, "w") as txtfile:

    # Write to document
    txtfile.write('\n'.join(lines))