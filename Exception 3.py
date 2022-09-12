print("START")
print("line 1")
print("line 2")
print("line 3")

try:
    print(10 / "hi")


# will not work due to error is not arithmetic

except ArithmeticError as refvar:
    print(refvar)
    print("block2")

print("line 4")
print("line 5")
print("line 6")
print("END")
