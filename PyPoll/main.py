
        # A complete list of candidates who received votes
        # The percentage of votes each candidate won
        # The total number of votes each candidate won
        # The winner of the election based on popular vote

# OS Module: This will will allow us to create paths across operating systems. 
import os

# CSV Module - Allows us to read csv files with python script. 
import csv

# File Path
csvpath = os.path.join('Resources', 'election_data.csv')

# Analysis Results
analysis_results = os.path.join("Analysis", "PyPoll_Analysis.txt")

# Vote Counter
Vote_Count = 0

# Define Lists/Directories
Stockham = "Charles Casper Stockham"
DeGette = "Diana DeGette"
Doane = "Raymon Anthony Doane"

#Inital Variables
Stockham_Percentage = 0
DeGette_Percentage = 0
Doane_Percentage  = 0
Stockham_Votes = 0
DeGette_Votes = 0
Doane_Votes = 0
Winner = ""
# Winners_Count = 0
# Winners_Percentage = 0
breakline = "---------------------------"

# Open as 
with open(csvpath) as csvfile:

    # CSV Reader
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # CSV header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    # Commands for Each Row
    for row in csvreader: 

        # Append Column Headers
        Candidate = row[2]

        # The total number of votes cast
        Vote_Count = Vote_Count + 1

        if Stockham in Candidate:
            Stockham_Votes += 1

        elif DeGette in Candidate:
            DeGette_Votes += 1

        elif Doane in Candidate:
            Doane_Votes += 1    

    if (Stockham_Votes > DeGette_Votes) and (Stockham_Votes > Doane_Votes):
        Winner = "Charles Casper Stockham"
        Winners_Count = Stockham_Votes
        Winners_Percentage = Stockham_Percentage

    elif (DeGette_Votes > Stockham_Votes) and (DeGette_Votes > Doane_Votes):
        Winner = "Diana DeGette"
        Winners_Count = DeGette_Votes
        Winners_Percentage = DeGette_Percentage

    elif (Doane_Votes > Stockham_Votes) and (Doane_Votes > DeGette_Votes):
        Winner = "Raymon Anthony Doane"
        Winners_Count = Doane_Votes
        Winners_Percentage = Doane_Percentage

# Print Summary Table
print(" ")
print("Election Results")
print(breakline)

# Print Total Ballot Count
print("Total Votes: ", str(int(Vote_Count)))
print(breakline)

# Print Votes for Stockham
print("Charles Casper Stockham: ", str(float(Stockham_Percentage))+"%", str(int(Stockham_Votes)))

# Print Votes for DeGette
print("Diana DeGette: ", str(float(DeGette_Percentage))+"%", str(int(DeGette_Votes)))

# Print Votes for Doane
print("Raymon Anthony Doane: ", str(float(Doane_Percentage))+"%", str(int(Doane_Votes)))
print(breakline)

# Print Winner
print("Winner: ", str(Winner))
print(breakline)