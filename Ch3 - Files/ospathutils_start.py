#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)
    
    # Check for item existence and type
    print("Item exists: ", path.exists("file.txt"))
    print("Item is a file: ", path.isfile("file.txt"))
    print("Item is a directory: ", path.isdir("file.txt"))
    # Work with file paths
    print("Item's path: ", path.realpath("file.txt"))
    print("Item's relative path: ", path.relpath("file.txt"))
    print("File's path and name: ", path.split(path.realpath("file.txt")))

    
    # Get the modification time
    # Convert (ctime) to a readable string, print it out
    t = time.ctime(path.getmtime("file.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("file.txt")))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("file.txt"))
    print("It has been", td, "since the file was modified")
    print("Or,", td.total_seconds(), "seconds")
  
if __name__ == "__main__":
    main()
