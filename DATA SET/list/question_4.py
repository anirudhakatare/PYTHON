num = [1, 2, 3, 4, 5]

grate = 0
second = 0

for i in range(len(num)):
    if num[i] > grate:
        second = grate
        grate = num[i]
    elif num[i] > second:
        second = num[i]

print(second)