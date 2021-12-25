# Challenge program

def palindrome(teststring):
    newstring = teststring[::-1]
    return teststring == newstring

running = True
while(running):
    teststring = input("Input a string: ")

    # Should we exit?
    if teststring == 'exit':
        break

    # Force to lowercase
    teststring = teststring.lower()

    # Remove punctuation
    newstr = ""
    for x in teststring:
        if x.isalnum():
            newstr += x
    
    # Return the result
    print("Palindrome?", palindrome(newstr))