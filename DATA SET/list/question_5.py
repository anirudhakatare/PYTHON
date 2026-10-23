num = [1,2,3,4,5,6,7,8,9]

even = []
odd = []

for i in range(len(num)):
    if((num[i]%2) == 0):
        n = num[i]
        even.append(n)
    else:
        o = num[i]
        odd.append(o)
        



print(even,odd)