# Import the data
import csv
import os

file_to_load=os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("analysis","election_analysis.txt")

#1. Initialize total vote counter
total_votes=0
#Candidate Options
candidate_options=[]
#candidate dictionary
candidate_votes={}

#Winning Candidate and Winning Count Tracker
winning_candidate= ""
winning_count=0
winning_percentage=0

#open election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #read and print out header row
    headers=next(file_reader)
    
    #print each row in csv file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes +=1

        # Print candidate name from each row
        candidate_name=row[2]

        #if canidate doesnt match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Track the candidates vote count
            candidate_votes[candidate_name]=0

        #Add a vote to candidates count
        candidate_votes[candidate_name]+=1
        
#the percentage of votes for each candidate by looping through the counts
#through candidate list
for candidate_name in candidate_votes:
    #retrieve vote count per candidate
    votes=candidate_votes[candidate_name]
    # calculate the percentage of votes
    vote_percentage=float(votes)/float(total_votes)*100
    
    #print out each candidates stats
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})')
   
    #Determine if votes are greater than winning count
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        #if true set
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
#print winning candidate stats
winning_candidate_summary=(f'------------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'------------------------------\n')
print(winning_candidate_summary)

#print candidate name with their percentage of votes
#print(f'{candidate_name} received {vote_percentage:.2f}% of the votes.')

#print candidate vote dictionary
#print(candidate_votes)
# Print the candidate list
#print(candidate_options)
#3. Print the total votes
#print(total_votes)
      
#with open(file_to_save,"w") as txt_file:
    #txt_file.write("Counties in the Election\n-------------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
    election_data.close()
