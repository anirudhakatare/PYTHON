num = [12,45,3,89,7]

grate = 0
for i in range(len(num)):
    if(grate < num[i]):
        grate = num[i]

small = grate


for i in range(len(num)):
    if(small > num[i]):
        small = num[i]
        


print(grate,"is the largest number in the list")
print(small,"is the smallest number in the list")