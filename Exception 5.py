print("START")
print("line 1")
print("line 2")
print("line 3")

try:
    print(10 / 0 )

except ArithmeticError as refvar:
    print(refvar)
    print("block1")

# will not work as previous exception will handle the error
except Exception as refvar:
    print(refvar)
    print("block2")

print("line 4")
print("line 5")
print("line 6")
print("END")