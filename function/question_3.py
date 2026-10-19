def prime (n):
    if n<=1:
        return "not a prime number"
    for i in range(2,n):
        if(n%i == 0):
            return "not a prime number"
        
    return "it is a prime number"
            
            


c = prime(int(input("enter your number: ")))

print(c)