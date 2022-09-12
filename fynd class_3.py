# adress
name = "shrikant"
print(id(name))
print(id(name[0]))
print(id(name[1]))
print(id(name[2]))

# list comprehensions

lis = [1,2,3,4,5]
lisempty = []
for x in lis:
    lisempty.append(x*x)

print(lisempty)

selist = [x*x for x in lis]
print(selist)

l1 = [1, 2, 3, 4]
l2 = [6, 7, 8, 9]render_template('login.html')

# zip creates a tuple of multiple tuples with elements in both lists
l3 = [x+y for x, y in zip(l1, l2)]
print(l3)
l4 = []
for x in range(0, len(l1)):
    l4.append(l1[x]+l2[x])
print(l4)

l5 = [l1[x]+l2[x] for x in range(len(l1))]
print(l5)
