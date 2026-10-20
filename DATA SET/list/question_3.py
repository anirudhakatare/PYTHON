num = [1,2,2,3,4,4,5]

common = []

for i in num:
    if i not in common:
        common.append(i)


print(common)