import os
import csv

# Function to read election data from a CSV file
def read_election_data(file_path):
    with open(file_path, "r") as file:
        reader = csv.Reader(file)
        data = [row for row in reader]
    return data

# Function to analyze votes
def analyze_votes(data):
    total_votes = len(data)
    vote_counts = {}
    
    for row in data:
        candidate = row['Candidate']
        if candidate in vote_counts:
            vote_counts[candidate] += 1
        else:
            vote_counts[candidate] = 1

    return total_votes, vote_counts

# Function to calculate vote percentages
def calculate_percentages(total_votes, vote_counts):
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in vote_counts.items()}
    return percentages

# Function to determine the winner based on popular vote
def determine_winner(vote_counts):
    winner = max(vote_counts, key=vote_counts.get)
    return winner

# Main function
def main():
    file_path = 'election_data.csv'  # Replace with your file path
    data = read_election_data(file_path)
    total_votes, vote_counts = analyze_votes(data)
    percentages = calculate_percentages(total_votes, vote_counts)
    winner = determine_winner(vote_counts)

    # Print the results
    print("Total number of votes cast:", total_votes)
    print("\nList of candidates who received votes and their vote details:")
    for candidate, votes in vote_counts.items():
        print(f"{candidate}: {votes} votes ({percentages[candidate]:.2f}%)")
    print("\nWinner of the election based on popular vote:")
    print(f"{winner} with {vote_counts[winner]} votes ({percentages[winner]:.2f}%)")

if __name__ == '__main__':
    main()