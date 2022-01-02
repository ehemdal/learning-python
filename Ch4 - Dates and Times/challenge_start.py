# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

def countdays(year, month, day):
    daycount = 0
    c = calendar.monthcalendar(year, month)
    for row in c:
        if row[day] != 0:
            daycount += 1
    return daycount

running = True
try: 
    while(running == True):
        print("Enter the day of the week:")
        print("0 - Monday")
        print("1 - Tuesday")
        print("2 - Wednesday")
        print("3 - Thursday")
        print("4 - Friday")
        print("5 - Saturday")
        print("6 - Sunday")

        entry = input("? ")

        if entry == "exit":
            running = False
            break
        day = int(entry)
        # Get the month and year
        month = input("Enter the month 1 - 12: ")
        month = int(month)
        year = input("Enter the year: ")
        year = int(year)

        result = countdays(year, month, day)
        print("There are " + str(result) + " days in the month")
except Exception as e:
    print("Invalid input")
    print(e)

