#! /usr/bin/env bash


#For this assignment you will use the commands recently learned. 
#Think awk, sort, cut, head, tail, etc to answer the following questions. 
#You should answer the questions by writing the commands in the program at 
#the appropriate places given below. And outputting the results.tab file. 

# these are bash flags the print out variables that get set when you
# run the program.
set -o nounset -o pipefail -o errexit -x

# This is where your project directory is, you should replace 
#what I have here with your own on the server

project=$/Users/ankeetashah/Documents/Barnard\ College/Semester\ 6/Genomics\ and\ Bioinformatics/projects
# fill in the date here and make sure you have created the appropriate directories as in the 
# paper. There should be a project folder as above with the additional subdirectories

date=2016-28-01

data=$/vega/edu/bc3308/users/abs2218/projects/data/$date
datafile=$data/linux.bed

results=$project/results/$date
resultsfile=$results/result.tab

# if the results directory doesn't exist, make it
if [[ ! -d $results ]]; then
    mkdir -p $results
fi

# Problem 1
# What is the region with the largest start position (2nd column)
#on any chromosome in HW2_bed.bed? 
#NOTE you can call the file $datafile since you defined it above

echo "Answer 1" > $resultsfile

sort -n -k2 $datafile | tail -n 1 >> $resultsfile
#I presorted based on the second column (which is the chromosome start position) and then printed out the last line which has the largest start position

# prints a blank line to the file to separate out answers
echo >> $resultsfile

# Problem 2
# What is the region with the largest end position on 
# chrY in HW2_bed.bed?
# Report this region in the format: chr12:1234-5678

echo "Answer 2" >> $resultsfile

# below here is where you should enter your commands to solve problem 1
awk '$1=="chrY"' $datafile | sort -n -k3 | awk 'BEGIN{OFS=""} {print $1,":"$2,"-"$3}'| tail -n 1 >> $resultsfile
#get all the regions on chrY, then sort by the third column (chromosme end), and then change the delimiters to print the last line in the desired format

echo >> $resultsfile

# Problem 3
# What is the longest region (end - start) in HW2_bed.bed?

echo "Answer 3" >> $resultsfile
awk 'NF > 0 { print $1 "\t" $2 "\t" $3 "\t" $4 "\t" ($3 - $2) }' $datafile| sort -n -k 5,5 | tail -n 1 >> $resultsfile
#create a new column (column 5) that is the region ($3-$2) and sort based on that to get the longest region.

echo >> results.tab

# Problem 4
# What is the longest region (end - start) in HW2_bed.bed with a 
# value (4th column) greater than 0.9 on chr13. Report the 
#header (1st line) in HW2_bed.bed as well as the region
echo "Answer 4" >> $resultsfile

awk -v threshold=0.9 'NR==1 || $4 > threshold && $1=="chr13"' $datafile | awk 'NF > 0 { print $1 "\t" $2 "\t" $3 "\t" $4 "\t" ($3 - $2) }' | sort -n -k 5,5 | awk 'NR==1; END{print}' >> $resultsfile

#repeating the creation of column 5, but first extracting the regions that have a threshold greater than 0.9 (column 4) and are on chr13. Then sorting, and getting the first and last line of the output.

echo >> $resultsfile

# Problem 5
# What are the regions that overlap this interval in HW2_bed.bed:
# chr12:5,000,000-6,000,000? Report regions so that they are 
#ordered by descending value (4th column), and the columns 
#are separated by commas rather than tabs

echo "Answer 5" >> $resultsfile

awk '$1=="chr12" &&  $2<6000000 && $3>5000000' $datafile | sort -n -r -k 4,4 | awk 'BEGIN {OFS=","} {print $1,$2,$3,$4}' >> $resultsfile
#extract regions on chr12 and overlap the region described above. These are then sorted and the lines that match are printed.

echo >> $resultsfile

# Problem 6
# What is the average value (4th column) of those regions 
#from HW2_bed.bed that overlap the region: chr12:5,000,000-6,000,000?

echo "Answer 6" >> $resultsfile

awk '$1=="chr12" &&  $2<6000000 && $3>5000000' $datafile | sort -n -r -k 4,4 |awk '{average = average+$4} END {print average/ NR}' >> $resultsfile

#taking the exact same commands as question 5 and then piping an average variable that keeps a running total of the thresholds in column 4 and then divides them by the number of rows to print out the average.

echo >> $resultsfile
 
