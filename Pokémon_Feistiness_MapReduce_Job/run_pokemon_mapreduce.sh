#!/bin/bash

# the above line specifies that we are 
# working with a bash script and needs to be executed in a 
# bash shell, especially when using ubuntu.

# Ensure Hadoop is working
hadoop version

# these are the Input and output paths; 
# the output is what gets created in the end
INPUT_FILE="pokemon.csv"
OUTPUT_DIR="pokemon_output"

# the following line of code remove previous output if 
# exists before running the Hadoop job
# hdfs dfs: This is the command-line interface for interacting with HDFS
# specifically, the”-r”, is for recursive deletion; 
# i.e; loops through the folder and delete everything.
# the ‘-rm’, is for stands for "remove." And  is used to delete files or directories in HDFS
# -skipTrash: just in case, you even want to go back to a  previous version, or this allows you to store a deleted version, in the trash directory. Else, the file/directory is removed permanently
# the ‘OUTPUT_DIR’ is the one create above, 
# which is deleted if it was already there, 
# that way, there is only one copy created at any time. *1,2
hdfs dfs -rm -r -skipTrash $OUTPUT_DIR





# for hdfs dfs -test -e $INPUT_FILE:
# hdfs dfs: is the command line used for interacting 
# with the Hadoop file

# -test: perform a test operation

# -e: checks if the directory exists

# $INPUT_FILE: is the variable holds the name of the CSV file we are working with.
# if [ $? -ne 0 ]; then ... fi :
# $?: is a shell variable that holds/expands to the exit status of the most recently executed foreground

# -ne 0: this is a comparison operator, and all it does is check if the exit status is “not equal” to 0

# echo: returns “Uploading pokemon.csv to HDFS...", provided the condition in the if statement is true

# hdfs dfs -put pokemon.csv $INPUT_FILE : this line uploads 
# the pokemon.csv file from the file system to the 
# HDFS location specified by $INPUT_FILE.
# which is slightly redundant because pokemon.csv, is already
# there. But if you don't add this line, you get an error message


# All in all, this is a long, complicated but necessary if statement. *3,4,5,6,7

hdfs dfs -test -e $INPUT_FILE
if [ $? -ne 0 ]; then
    echo "Uploading pokemon.csv to HDFS..."
    hdfs dfs -put pokemon.csv $INPUT_FILE
fi
# DISCLAIMER
# for the above code, some part where taken from lecture note, but other parts, although their working is understood, Gemini helped find, add and organise the missing parts.
# the goal of the above code, is to act as a fail safe, that checks where the code is not working.
# in this case, all that it does, is let you know, if it is not reading or finding the “pokemon.csv” file




# the following Hadoop streaming specifies 
# the input, output, mapper, reducer, 
# and as well specifies the 
# file used for the input, output, mapper and reducer. *8,9

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
    -D mapreduce.framework.name=yarn \
    -D mapreduce.job.reduces=2 \
    -input $INPUT_FILE \
    -output $OUTPUT_DIR \
    -mapper mapper1.py \
    -reducer reducer.py \
    -file mapper1.py \
    -file reducer.py



# the code: hdfs dfs -getmerge $OUTPUT_DIR results.csv. 
# is supposed to Fetch results from HDFS

# hdfs dfs: this is the the HDFS command-line interface
# -getmerge: this is supposed to downloads multiple files from an HDFS directory and merges them into a single local file.
# $OUTPUT_DIR: the path in question to the directory, that contains the files that will be merged.
# results.csv: name of the resulting file that will be created to store the merged data
hdfs dfs -getmerge $OUTPUT_DIR results.csv

# this prints the echo part, 
# if everything worked correctly. 
# And displays the results.
echo "MapReduce job completed. Final results:"
cat results.csv

# reference for all the code in the readme file.
# The sections marked with (*) indicate 
# where there is code sourced, 
# referenced, or where the understanding 
# was derived from another source other than myself.
