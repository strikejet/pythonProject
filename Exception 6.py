print("START")
print("line 1")
print("line 2")
print("line 3")

# accident
list1 = [1, 2, 3, 4, 5]
# compiler --> left to right   so it will pick first exception
try:
    print(list1[10] / 0 )

# hospital 1
except ArithmeticError as refvar:
    print(refvar)
    print("block1")

# hospital 2
except IndexError as refvar:
    print("block 2")
    print(refvar)

# hospital 3
# will not work as second will handle
except Exception as refvar:
    print(refvar)
    print("block 3")

print("line 4")
print("line 5")
print("line 6")
print("END")