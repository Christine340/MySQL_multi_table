#Assignment 2
#Database Design
#Jiahui Yi

#The original data file is called: originalData.csv
#The clean data generated from this python code is called: cleanData.csv

#This code is to clean a data that include NYC high school SAT average scores
#Since we only want to analyze SAT score, so I delete the first column "DBN"
#and records with less than 5 students are marked "s" in original data
#I change all "s" into 0. since less than 5 records will not generate a reliable
#data analysis in a statistical level. 

import re
#open and read original file
f = open("originalData.csv", "r")
p = re.compile(r"\s+")

#create a empty 2D list
file2Dlist=[]
for line in f:
    #print(line)
    line=line[:-1]
    #remove first column(since first column is not useful for data analysis)
    arr=line.split(",")
    arr=arr[1:]
    #replace all "s" in excel into "0"
    #since "s" does not make sense in data analysis
    for i in range(len(arr)):
        if arr[i]=="s" :
            arr[i]="0"
    
    file2Dlist.append(arr)
#print(file2Dlist)
f.close()
#write clean data to a new file
f = open("cleanData.csv", "w")

#loop through each line of data
for lineData in file2Dlist:

    #make a string with comma-separated values
    thisLineWithCommas = ",".join(lineData) #join all list elements with a comma
    thisLineWithCommas = thisLineWithCommas + "\n" #add a line break at the end of the line

    f.write(thisLineWithCommas)

#close the file
f.close()
