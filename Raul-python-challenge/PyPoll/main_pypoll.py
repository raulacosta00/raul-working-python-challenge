import os
import csv

pypoll_csv = os.path.join("Resources","election_data.csv")

# Delcaring Variables to use for later
total_votes = 0
candidates = []
candidates_percentage = []
khan_votes = 0
khan_percent = []
correy_votes = 0
correy_percent = []
li_votes = 0
li_percent = []
otooley_votes = 0
otooley_percent = []

with open(pypoll_csv , "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = "," )
    csv_header = next(csvfile)

    # Loop that will run through the csv file looking for the data
    for row in csv_reader:
           #Total number of votes
            if row[0] != " ":
                total_votes = total_votes + 1
            #Total votes per candidate
            if row[2] not in candidates:
                candidates.append(row[2])
            if row[2] == "Khan":
                khan_votes = khan_votes + 1
            if row[2] == "Correy":
                correy_votes = correy_votes + 1
            if row[2] == "Li":
                li_votes = li_votes + 1
            if row[2] == "O'Tooley":
                otooley_votes = otooley_votes + 1

#Calculations for percentages

khan_percent = round(((khan_votes / total_votes)* 100),3)
candidates_percentage.append(khan_percent)

correy_percent = round(((correy_votes / total_votes)* 100),3)
candidates_percentage.append(correy_percent)

li_percent = round(((li_votes / total_votes)* 100),3)
candidates_percentage.append(li_percent)

otooley_percent = round(((otooley_votes / total_votes)* 100),3)
candidates_percentage.append(otooley_percent)

# Max Percent
max_percent = max(candidates_percentage)
max_percent_index = candidates_percentage.index(max_percent)

# Winner
winner = candidates[max_percent_index]

# Print results

print("Election Results")
print("----------------")
print("Total Votes: " + str(total_votes))
print("----------------")
print("Khan: " + str(khan_percent)+ " "+ str(khan_votes))
print("Correy: " + str(correy_percent)+ " "+ str(correy_votes))
print("Li: " + str(li_percent)+ " "+ str(li_votes))
print("O'Tooley: " + str(otooley_percent)+ " "+ str(otooley_votes))
print("Winner: " + str(winner))

pypoll_analysis = os.path.join ("Analysis", "PyPollAnalysis.txt")

with open(pypoll_analysis, "w") as text_file:

    text_file.write("Election Results \n")
    text_file.write("---------------- \n")
    text_file.write("Total Votes: " + str(total_votes) + "\n")
    text_file.write("---------------- \n")
    text_file.write("Khan: " + str(khan_percent)+ " "+ str(khan_votes) + "\n") 
    text_file.write("Correy: " + str(correy_percent)+ " "+ str(correy_votes) + "\n")
    text_file.write("Li: " + str(li_percent)+ " "+ str(li_votes) + "\n")
    text_file.write("O'Tooley: " + str(otooley_percent)+ " "+ str(otooley_votes) + "\n")
    text_file.write("Winner: " + str(winner) + "\n")

