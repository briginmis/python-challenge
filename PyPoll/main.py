import os
import csv

#obtain filepath
filepath = os.path.join("Resources","election_data.csv")

#state variables
vote_count = 0
vote_dict = {}

#open and read the file
with open(filepath,"r") as election:
    csvreader=csv.reader(election, delimiter = ",")
    
    #ignore the first row
    header = next(csvreader)

    #loop through data
    for row in csvreader:
        #read candidate name in data
        candidate = str(row[2])
        #count votes
        vote_count += 1
        #add candiates and number of votes to dictionary
        if candidate in vote_dict:
            x = vote_dict[candidate]
            x += 1
            vote_dict[candidate] = x
        else:
            vote_dict[candidate] = 1

#write results in text file
#obtain filepath
textpath = os.path.join("Analysis","poll.txt")

#open textpath to write in 
with open(textpath, "w") as f:
    f.write("Election Results")
    f.write('\n'"-------------------------")
    f.write('\n'f"Total Votes: {vote_count}")
    f.write('\n'"-------------------------")

    #print results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {vote_count}")
    print("-------------------------")

    #loop through candidates and print results
    winner_vote = 0
    for can in vote_dict:
        vote_percent = round(vote_dict[can] / vote_count * 100,3)
        print(f"{can}: {vote_percent}% ({vote_dict[can]})")
        f.write('\n'f"{can}: {vote_percent}% ({vote_dict[can]})")
        #determine winner
        if vote_percent > winner_vote:
            winner_vote = vote_percent
            winner = can
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    f.write('\n'"-------------------------")
    f.write('\n'f"Winner: {winner}")
    f.write('\n'"-------------------------")




