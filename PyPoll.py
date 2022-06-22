# Import the data
import csv
import os

file_to_load=os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("analysis","election_analysis.txt")
#open election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
#read and print out header row
    headers=next(file_reader)
    print(headers)
        

#with open(file_to_save,"w") as txt_file:
    #txt_file.write("Counties in the Election\n-------------------------------\nArapahoe\nDenver\nJefferson")

#1. The total number of votes casted
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
# Close the file
    #election_data.close()
