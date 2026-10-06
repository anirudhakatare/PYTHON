num = int(input("enter the number you want to find the" \
"you want to find its length: "))
count = 0
while num >0:
    num = num//10
    count = count+1


print(count)