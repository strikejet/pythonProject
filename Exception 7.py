print("START")
print("line 1")
print("line 2")
print("line 3")

try:
    print(10 / 0)

# even though block 1 will tackle the error you should not use this type of program
# as exception is extensive class to use all the errors and
# it should be programmed at the end after special(sub) exceptions
# rule - You should go for specific to generic classes to handle exceptions
# other languages will give error at such uses

except Exception as refvar:
    print(refvar)
    print("block 1")

except ArithmeticError as refvar:
    print(refvar)
    print("block 2")

# will not work as previous exception will handle the error


print("line 4")
print("line 5")
print("line 6")
print("END")
