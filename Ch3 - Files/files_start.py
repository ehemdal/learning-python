#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist

    
    # Open the file for appending text to the end
    file = open("file.txt","a+")

    # write some lines of data to the file
    for i in range(10):
        file.write("This is a line of text\n")
    
    # close the file when done
    file.close()
    
    # Open the file back up and read the contents
    myfile = open("file.txt", "r")
    if myfile.mode == "r":
        contents = myfile.read()
     #   contents = myfile.readlines()
     #   for x in contents:
     #       print(x)
    
    print(contents)

    
if __name__ == "__main__":
    main()
