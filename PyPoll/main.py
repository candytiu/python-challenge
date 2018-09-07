import os
import csv
from collections import Counter
csvpath = os.path.join("election_data.csv") 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    csvlist = list(csvreader)

    #creating lists
    voters = []
    candidate = []


    #first loop
    for row in csvlist:
        voters.append(row[0])
        candidate.append(row[2])

    #variables
    total_votes = len(voters)
    counter = Counter()
    for name in candidate:
        counter[name] += 1

    print("Election Results")
    print("---------------------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------------------")
    
    percentage_khan = (counter['Khan'] / total_votes) * 100
    percentage_correy = (counter['Correy'] / total_votes) * 100
    percentage_li = (counter['Li'] / total_votes) * 100
    percentage_ot = (counter["O'Tooley"] / total_votes) * 100

    results = {'Khan': percentage_khan, 'Correy': percentage_correy, 'Li': percentage_li, "O'Tooley": percentage_ot}

    print('Khan: {0:.3f}% ({1})'.format(percentage_khan, counter['Khan']))
    print('Correy: {0:.3f}% ({1})'.format(percentage_correy, counter['Correy']))
    print('Li: {0:.3f}% ({1})'.format(percentage_li, counter['Li']))
    print("O'Tooley: {0:.3f}% ({1})".format(percentage_ot, counter["O'Tooley"]))

    percentages = list()
    percentages.append(percentage_khan)
    percentages.append(percentage_correy)
    percentages.append(percentage_li)
    percentages.append(percentage_ot)

    winner = max(percentages)
    print("---------------------------------------")
    print(f"Winner: {winner}")      
    print("---------------------------------------")

