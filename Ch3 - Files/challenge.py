import os
from os import path

# Get a list of all the files in the current directory
dirlist = os.listdir()

# Start a running total of byte count for all files
bytecount = 0
# For each file, add its byte count to the total.  Skip directories
for file in dirlist:
    if path.isfile(file):
        bytecount += path.getsize(path.realpath(file))
print("Bytecount = " + str(bytecount))

# Then create a new subdirectory called "results"
if path.exists("results") == False:
    os.mkdir("results")

# In this directory, create a file called "results.txt"
outfile = open("./results/results.txt", "w+")

# In results.txt, print the "Total bytecount" and a list of the filenames
outfile.write("Total Bytecount: " + str(bytecount) + "\n")
outfile.write("File List\n---------\n")
for file in dirlist:
    if path.isfile(file):
        outfile.write(file + "\n")

outfile.close()
