import os
import csv

# Function to read election data from a CSV file
def read_election_data(file_path):
    with open(file_path) as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        data = [row for row in reader]
    return data

# Function to analyze votes
def analyze_votes(data):
    total_votes = len(data)
    vote_counts = {}
    
    for row in data:
        candidate = row[2]
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

# Function to write results to a text file
def write_results_to_file(file_path, total_votes, vote_counts, percentages, winner):
    with open(file_path, 'w') as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")
        for candidate, votes in vote_counts.items():
            file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")

# Main function
def main():
    input_file_path = 'resources/election_data.csv'   
    output_dir_path = 'analysis'
    output_file_path = os.path.join(output_dir_path, 'election_analysis.txt')
    
    if not os.path.exists(input_file_path):
        print(f"File {input_file_path} does not exist.")
        return
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir_path, exist_ok=True)

    data = read_election_data(input_file_path)
    total_votes, vote_counts = analyze_votes(data)
    percentages = calculate_percentages(total_votes, vote_counts)
    winner = determine_winner(vote_counts)

    # Print the results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in vote_counts.items():
        print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")

    # Write the results to a text file
    write_results_to_file(output_file_path, total_votes, vote_counts, percentages, winner)
    

if __name__ == '__main__':
    main()