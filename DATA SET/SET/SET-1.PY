a = {3,5,6,7,8}

a.add(45)
print(a)
a.remove(5)
print(a)

b = {6,7,45,2,4,56}

c= a.union(b)
print(c)

g=a.intersection(b)
print(g)

f=a.difference(b)
print(f)
h=a.symmetric_difference(b)

print(h)