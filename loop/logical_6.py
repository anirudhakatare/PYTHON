n = int(input("enter the number: "))
large =0

while n>0:
    digit = n %10
    if (digit > large):
        large = digit
    digit = digit //10
    n = n//10
print(large)