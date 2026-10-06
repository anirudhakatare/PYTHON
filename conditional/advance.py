day = int(input("enter the day: "))
month = int(input("enter the month: "))
year = int(input("enter the year: "))

if(day<=31 and day>=1):
    if(month<=12 and month>=1):
        if((year %4)==0):
            print("it is an valid date according to leap year")
        else:
             (print("not valid according to leap year"))