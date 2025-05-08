#!/usr/bin/env python3

# The above line Specifies that the script should be executed using Python 3. 
# env helps locate the correct Python version in different environments.


# First we need to import sys module. sys.stdin can 
# be used to get input from the command line directly. 
# It used for standard input. 
# It internally calls the input() method. Furthermore, it, 
# also, automatically adds ‘\n’ after each sentence *1
import sys

# this is used for reading a csv file *2
import csv


# this code allows to read the lines in csv. 
# The for loop, allows to loop through the 
# csv file, without needing 
# to go through the same process again and again.*3,4
for line in sys.stdin:
    #this Removes the leading/trailing spaces for a very line.*5
    line = line.strip()

    # this line of the code is for parsing 
    # the single line as a csv formatted data
    # google and gemini, did help me understand WHY! it works.*6,7
    reader = csv.reader([line])

    #this for loop  allows to extract the 
    # required data in reality, I had to do 
    # some googling and asking Gemini several questions, 
    # because the formatting of the code does 
    # not make sense but it works. 
    # basically, what it does it selects 
    # the name, type1, type2, attack and weight, 
    # based on the index of the column. 
    # But because it is a csv file, ‘row[]’ is used 
    # instead of ‘.column[]’

    for row in reader:
        try:
            # Extract necessary fields based on the csv 
            # file with correct indices
            name = row[30]  # Pokémon Name
            type1 = row[36]  # Primary Type
            type2 = row[37] if row[37].strip() else "unknown"  # Secondary Type (replace empty values with "unknown")
            attack = float(row[19])  # Attack Points
            weight = float(row[38])  # Weight in kg

            # this code is used to handle errors 
            # resulting in division by zero
            # the condition here is that weight must 
            # be greater than 0
            if weight > 0:
                # Feistiness (F = attack / weight)
                feistiness = round(attack / weight, 2)
                print(f"{type1},{type2},{name},{feistiness}")

        # this for just in case there is an error. 
        # that way the code does not stop. *8,9,10
        except (ValueError, IndexError):
            continue  # this for skipping invalid rows
        
        # reference for all the code in the readme file.
        # The sections marked with (*) indicate 
        # where there is code sourced, 
        # referenced, or where the understanding 
        # was derived from another source other than myself.


