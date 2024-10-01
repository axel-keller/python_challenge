import os
import csv

# Input and output file paths
csvpath = os.path.join('..', 'Resources', 'election_data.csv') # Input file path
file_to_output = os.path.join("../analysis", "election_analysis.txt") # Output file path

# Initialize total votes and other necessary variables
total_votes = 0
candidates = {}
winner = ""
winning_count = 0

# Open the input CSV file and process it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header (skip it)
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment the total vote count (excluding header)
        total_votes += 1

        # Get the candidate's name from the row (3rd column)
        candidate_name = row[2]

        # If the candidate is not in the dictionary, add them with an initial vote count of 0
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates[candidate_name] += 1

# Open the output text file to save the results
with open(file_to_output, "w") as txt_file:

    # Print and write the election results header
    election_results = (
        f"Election Results\n"
        "--------------------------\n"
        f"Total Votes: {total_votes}\n"  # Print the total votes here
        "--------------------------\n"
    )
    print(election_results)
    txt_file.write(election_results)

    # Loop through the candidates to calculate vote percentages and determine the winner
    for candidate, votes in candidates.items():
        # Calculate the vote percentage
        vote_percentage = (votes / total_votes) * 100

        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine if this candidate has the most votes
        if votes > winning_count:
            winning_count = votes
            winner = candidate

    # Print and write the winner summary
    winner_summary = (
        "--------------------------\n"
        f"Winner: {winner}\n"
        "--------------------------\n"
    )
    print(winner_summary, end="")
    txt_file.write(winner_summary)
