# using string

n = int(input("enter the the number yo want to reverse: "))
new =""
while n >0:
    digit = str(n%10)
    new = new + digit
    n = n//10
print(new)


# without using string

n = int(input("enter the the number yo want to reverse: "))
rev = 0
while n >0:
    digit = n%10
    rev = rev * 10 + digit 
    n = n//10
print (rev)
