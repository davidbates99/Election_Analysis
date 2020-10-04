#Module 3 - PyPoll 
    # The data we need to retrieve.
    # 1. The total number of votes cast
    # 2. a complete lsit of candidates who recieved votes
    # 3. Total # of votes each candidates recieved
    # 4. % of votes each candidate won
    # 5. Winner of the election based on popular vote

import csv

file2load = "Resources\election_results.csv"
file2save = open("Analysis\election_analysis.txt", "w")

with open(file2load) as ElectionData:
    csv_filereader = csv.reader(ElectionData)

    headers = next(csv_filereader)
    print(headers)

    for row in csv_filereader:
        print(row)

ElectionData.close
