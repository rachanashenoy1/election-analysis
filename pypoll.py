# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)


#import csv
#import csv
#dir()

# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()

# Open the election results and read the file
#with open(file_to_load) as election_data:

     # To do: perform analysis.
     #print(election_data)

#import os
#import csv
#file_to_load = os.path.join("Resources","election_results.csv")
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

#Condense the code
#file_to_save = os.path.join("Analysis","election_analysis")
#with open(file_to_save,'w') as txt_file:
    #txt_file.write ('Hello World, ')
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
    #Write three counties to the file
    #txt_file.write('Counties in the election')
    #txt_file.write('\n-------------------------\n')
    #txt_file.write("Arapahoe\nDenver\nJefferson")

#import dependencies
import os
import csv
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis','election_analysis.txt')
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
      # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
     # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)


#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote