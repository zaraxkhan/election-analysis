# Import the data
import csv
import os

file_to_load=os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("analysis","election_analysis.txt")

#Initialize total vote counter
total_votes=0
#Candidate Options
candidate_options=[]
#candidate dictionary
candidate_votes={}

#Initialize county list and dictionary
county_options=[]
county_votes={}

#Winning Candidate and Winning Count Tracker
winning_candidate= ""
winning_count=0
winning_percentage=0

#Track largest county and county voter turnout
largest_county=""
voter_turnout=0


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

        #Extract county name from each row
        county_name=row[1]

        #if canidate doesnt match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Track the candidates vote count
            candidate_votes[candidate_name]=0

        #Add a vote to candidates count
        candidate_votes[candidate_name]+=1

        #add count names that dont repeat in county list
        if county_name not in county_options:
            county_options.append(county_name)

            #Track the county's vote count
            county_votes[county_name]=0

        #add vote to county's vote count
        county_votes[county_name]+=1
    
#save results to text file
with open(file_to_save,"w") as txt_file:
    election_results=(
        f'Election Results\n'
        f'-------------------------\n'
        f'Total Votes:{total_votes:,}\n'
        f'-------------------------\n\n'
        f'County Votes:\n')

    print(election_results, end="")

    #save finaly vote count to text file
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        counties=county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage=(float(counties)/float(total_votes))*100

         # 6d: Print the county results to the terminal.
        county_results=(
            f'{county_name}:{county_vote_percentage:.1f}% ({counties:,})\n')
        
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (counties>voter_turnout):
            voter_turnout=counties
            largest_county=county_name

    # 7: Print the county with the largest turnout to the terminal.
    county_largest_results=(
        f'-------------------------\n'
        f'Largest County Turnout: {largest_county}\n'
        f'-------------------------\n')
    
    print(county_largest_results)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_largest_results)       
    
    #the percentage of votes for each candidate by looping through the counts
    #through candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count per candidate
        votes=candidate_votes[candidate_name]
        # calculate the percentage of votes
        vote_percentage=float(votes)/float(total_votes)*100
                
        #print out each candidates stats
        candidate_results=(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(candidate_results)

        #save file
        txt_file.write(candidate_results)
            
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

    #save file to txt file
    txt_file.write(winning_candidate_summary)

# Close the file
election_data.close()