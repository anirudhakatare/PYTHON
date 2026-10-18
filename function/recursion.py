def fib(n):
    if (n==1 or n==0):
        return n
    return fib(n-2) + fib(n-1)




o = fib(16)
print(o)





def fact(r):
    if (r==1 or r==0):
        return 1
    return r * fact(r-1)
    
    
p = fact(5)


print(p)