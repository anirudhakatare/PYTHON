def sum(n):
    add = 0 
    while n > 0:
        d = n%10
        add= d + add
        n = n//10
    return add


c = sum(int(input("enter your number: ")))

print(c)