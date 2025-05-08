#!/usr/bin/env python3

# The above line Specifies that 
# the script should be executed using Python 3. 
# env helps locate the correct Python 
# version in different environments.
import sys

# This line helps keep track of the first line, that way, 
# when the final csv is created, it will have headers
first_line = True  

# Print headers at the beginning
print("type1,type2,name,feistiness")

# this line of code allows to store all the Pokémon data 
# in a list that way we can sort it latter.
# it would have been best to create a 
# dictionary, that way each data can be 
# accessed individually and rapidly, which 
# also helps with any other computational process.
pokemon_data = []  


# this code allows to read the lines in csv. 
# The for loop, allows to loop through the csv 
# file, without needing to go 
# through the same process again and again
for line in sys.stdin:

    # this Removes the leading/trailing 
    # spaces & newline characters
    line = line.strip()

    # this here is where the reducer, 
    # begins extracting the pokemon data
    try:

        # this line of code, splits the above created 
        # line in four values/variables: 
        # type1, type2, name and feistiness
        type1, type2, name, feistiness = line.split(',')

        # this line is a bit redundant, because in 
        # the mapper we have already specified that, feistiness, 
        # will be rounded to 2 values. But just to be sure
        feistiness = float(feistiness)

        # this line, replace the  NaN/nan or empty type2 
        # with "unknown". Again redundant, but just to be sure
        # it also takes into account the empty spaces. 
        # if there are any
        if type2.strip() == "" or type2.lower() == "nan":
            type2 = "unknown"
        
        # # this line append the found type1, type2, 
        # name and feistiness, 
        # to pokemon_data for latter sorting. 
        pokemon_data.append((name, type1, type2, feistiness))
    except ValueError:
        continue #  this indicates that if there any errors, it should continue and not stop

"""
this code sorts the resulting pokemon_data by name.
realistically this code does not make sense, 
first because I had never used it in my entire life, 
second because it does not make sense.
however, it works. It assumes that [name] will be at index 2,
lambda x: x[2], the sorting key is the third item in the resulting tuple. 
Basically, inside the list made of brackets [] 
there is something made of parentheses (), 
which is called a tuple. 
not sure why, but still it works.
However, you might need to change x[2] to x[0] if name 
not sorted. But either way, you get sorted values.
"""
pokemon_data.sort(key=lambda x: x[2])  

# this line prints all Pokémon in sorted order
for name, type1, type2, feistiness in pokemon_data:
    print(f"{type1},{type2},{name},{feistiness}")

# reference for all the code in the readme file.
# The sections marked with (*) indicate 
# where there is code sourced, 
# referenced, or where the understanding 
# was derived from another source other than myself.