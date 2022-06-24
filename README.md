# Election-Analysis
## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.7, Visual Studio Code 1.68.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the votes and 85,213 number of votes.
  - Diana DeGette received 73.8% of the votes and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the votes and 11,606 number of votes.
- The winner of the election was:
  - Candidate Diana DeGette, who received 73.8% of the votes and 272,892 number of votes.

## Challenge Overview
The Colorado Board of Elections has requested additional information to complete the election audit.
1. Get the voter turnout for each county.
2. Calculate the percentage of votes from each county out of the total count.
3. Determine the county with the highest voter turnout.

## Challenge Results
The analysis of this election show the following results:
- The counties that were a part of this election were:
  - Jefferson County
  - Denver County
  - Arapahoe County
- The voter turnout per county were:
  - Jefferson County made up 10.5% of the voter turnout and 38,855 of the citizens showed up to vote.
  - Denver County made up 82.8% of the voter turnout and 306,055 of their citizens showed up to vote.
  - Arapahoe County made up 6.7% of the voter turnout and 24,801 citizens showed up to vote.
  
## Challenge Summary
This script can be used for future election reading results. By simply changing the file location, varible verbage to match with whatever election is going on, and altering the row numbers to match with the new data set, this script will be ready for future use. If any additional markers want to be added, then defining the varibles and copying lines 58-66 can be followed to count the rows. As well as lines 82-112 in order to find the winner of the varible. 

### Examples for Script Modification
This script can be used for a state wide governor election. By importing the governor race election data and defining the new rows that will be used to gather the candidate names and county names, the script should be good to go to gather the election results for a statewide race.

This script can also be used for a much bigger race, such as a presidential race. For this, the election data for the preseidential race will have to be imported. The varibles may need to be changed. The candidate option varibles can stay the same, however the row data for the candidate names will have to be altered to match the data set. The county varibles can also stay the same if county data is wanting to be recorded, however I would say changing the county varibles to state varibles instead may get a better picture of the race. Additionally, chaning the row count to match the state in which the vote was casted would have the dataset reflect the state votes for the presidential race. This would work best to count the popular vote per state. 
