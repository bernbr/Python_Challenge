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

# Initial Variables
Profit_Start = 0
Month_Count = 0
Total_Profit = 0
Profit_Change = 0
Total_Change = 0

# Open as 
with open(csvpath) as csvfile:

    # CSV Reader
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # CSV header
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Commands for Each Row
    for row in csvreader: 

        # Append Column Headers
        Date.append(row[0])
        Profit.append(row[1])
        
        # Count the rows for the total number of months
        Month_Count = Month_Count + 1

        # Profit Total
        Total_Profit = Total_Profit + int(row[1])
        
        # Average Profit Change
        nProfit = int(row[1])
        Monthly_Profit_Change = nProfit - Profit_Start
        Change.append(int(Monthly_Profit_Change))
        Total_Change = Total_Change + Monthly_Profit_Change

        Profit_Start = nProfit
    # Average Change
    Average_Change = Total_Change / Month_Count

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

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
print("Average Change: ", "$"+str(int(Average_Change)))

# The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: ", Increase_Date, "($"+str(int(Greatest_Increase))+")")

# The greatest decrease in profits (date and amount) over the entire period
print("Greatest Increase in Profits: ", Decrease_Date, "($"+str(int(Greatest_Decrease))+")")

# Text Output
lines = ["Financial Analysis", "-------------------------------------", "Total Months: "+str(int(Month_Count)), "Total: "+"$"+str(int(Total_Profit)), "Average Change: "+"$"+str(int(Average_Change)), "Greatest Increase in Profits: "+Increase_Date+" "+"($"+str(int(Greatest_Increase))+")", "Greatest Increase in Profits: "+Decrease_Date+" "+"($"+str(int(Greatest_Decrease))+")"]

# Output file
output = os.path.join("Analysis", "output.txt")

# Wrtie output as text file
with open(output, "w") as txtfile:

    # Write to document
    txtfile.write('\n'.join(lines))