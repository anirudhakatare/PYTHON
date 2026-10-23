num = [1,1,2,2,3,3]

new =[]

for i in num:
    if(i not in new):
        n = i
        new.append(n)
print(new)