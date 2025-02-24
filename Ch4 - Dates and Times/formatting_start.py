#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 

    
    #### Date Formatting ####
    now = datetime.now()

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("%a %B %d %Y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("%c which is %x and %X"))

    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  

if __name__ == "__main__":
    main()
