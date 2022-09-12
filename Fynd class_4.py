# tuple
# characteristics --> immutable, indexing, duplicating, hetero, slice


tup1 = ()
tup2 = (1, 2, "python")

tup3 = ("dive")  # gives error due to there is only one element

# list inside a tuple and vice versa

tup5 = (1, 2, [2, 4, 6])
lis1 = [5, 6, ("one", "two")]
print(tup5)
print(lis1)

# You can't change elements in tuple but if there is mutable data type inside tuple ,
# you can change that example list inside tuple
tup5[2][1] = 5
print(tup5)

# tuple methods --> count, index

tupl1 = (1, 54, 30, 30, 45)
print(tupl1.count(30))
print(tupl1.index(30))

# concatenation
tupl3 = (1, 2, 3, 4, 5)
tupl4 = (1, 2, 3, 4, 5)
restupl = tupl3 + tupl4
print(restupl)


# There is no comprehension in tuple but we can use generator for creating tuples
tupl5 = tuple(i+j for i, j in zip(tupl3, tupl4))
tupl6 = tuple(tupl3[i]+tupl4[i] for i in range(5))

print(tupl5)
print(tupl6)

# list inside tuple
tup5 = (1, 2, [10, 20])
tup5[2][0] = 40
print(tup5)    # works that is you can change elements of list inside a tuple

# methods
tupl1 = (10, 20, 30, 30, 30)
print(tupl1.count(30))
print(tupl1.index(20))

# add 2 tuples
# tp1 = {1, 2, 3, 4, 5}
# tp2 = {1, 2, 3, 4, 5}
# resulttup1 = tp1 + tp2
# print(resulttup1)   #dose not work


# Dictionary ->> {}, mutable(hybrid), duplication not allowed
# creation part
# {key: value}

# remaining is written in notebook


