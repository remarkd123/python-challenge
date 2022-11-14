# import modules
import os
import csv
# from csv import DictReader

# set files paths
ballot_csv = os.path.join("Resources", "election_data.csv")
# Assign a variable to save the file to a path.
results_out = os.path.join("Analysis", "election_analysis.txt")

# Lists to store data
ballot_id = []
ballot_county = []
ballot_vote = []

# tally of the total vote
tally_vote = 0

# List of candidates
candidate_list = []

# tally of votes for each candidate
candidate_votes = {}

# Track the winning candidate, vote count, and percentage of the vote
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(ballot_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header row
    headers = next(csvreader)

    for row in csvreader:
        
        # add to the total vote count
        tally_vote += 1

        # Add date
        ballot_id.append(row[0])
        
        # trans amount list
        ballot_county.append(row[1])
        
        # Sum transactions
        ballot_vote.append(row[2])
        candidate_name = row[2]
        
        #determine if the candidate has been counted already
        if candidate_name not in candidate_list:
            
            # if not, add the candidate's name to the list, and set vote counter to zero
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # if candidate exists on the candidate_list, then increase the vote by one
        candidate_votes[candidate_name] += 1

# Save the results to a text file.
with open(results_out, "w") as txt_file:

    # Print out the final vote count.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {tally_vote}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Export the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_list:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(tally_vote) * 100
    
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n")

        # Print each candidate, their voter count, and percentage.
        print(candidate_results)
    
        # Save each candidate's results to the text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
    #   # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
             # If true then set winning_count = votes and winning_percent =
             # vote_percentage.
             winning_count = votes
             winning_percentage = vote_percentage
             # And, set the winning_candidate equal to the candidate's name.
             winning_candidate = candidate_name
    
    # #  Print the winning candidate, vote count and percentage to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)