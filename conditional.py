# basic question 

# num = int(input("enter the number: "))
# if((num%2)==0):
#     print("the number is even")
# else:
#     print("odd number")



# intermediate question

# num1= int(input("enter the first number"))
# num2= int(input("enter the second number"))
# num3= int(input("enter the third number"))


# if(num1>num2 and num1 > num3):
#     print( num1,"is the largest number")
# elif(num2> num1 and num2 > num3):
#     print(num2,"is the largest number")
# elif(num3>num1 and num3>num2):
#     print(num3,"is the largest number")
# else:
#     print("all are equal")


#advance questions

day = int(input("enter the day: "))
month = int(input("enter the month: "))
year = int(input("enter the year: "))

if(day<=31 and day>=1):
    if(month<=12 and month>=1):
        if((year %4)==0):
            print("it is an valid date according to leap year")
        else:
             (print("not valid according to leap year"))
