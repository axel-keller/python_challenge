#import os / csv
import os
import csv
#define path in/out
csvpath = os.path.join('', 'Resources', 'election_data.csv')
file_to_output = os.path.join("analysis", "election_analysis.txt")
# define variables
total_votes = 0
candidates = {}
winner = ""
winning_count = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#header
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        candidates[candidate_name] += 1
#output in txt file
with open(file_to_output, "w") as txt_file:

    election_results = (
        f"Election Results\n"
        "--------------------------\n"
        f"Total Votes: {total_votes}\n"  
        "--------------------------\n"
    )
    print(election_results)
    txt_file.write(election_results)


    for candidate, votes in candidates.items():
        vote_percentage = (votes / total_votes) * 100

        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results)
        txt_file.write(candidate_results)

        if votes > winning_count:
            winning_count = votes
            winner = candidate

    winner_summary = (
        "--------------------------\n"
        f"Winner: {winner}\n"
        "--------------------------\n"
    )
    print(winner_summary, end="")
    txt_file.write(winner_summary)
