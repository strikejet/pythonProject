# Nested try and except
print("START")
print("line 1")
print("line 2")
print("line 3")

try:
    print(10 / 0)
    # this try will not be executed as error from upper print will transfer the command to outer box
    try:
        print(10 / 0)
    except Exception:
        print("Inner")


except Exception as refvar:
    print(refvar)
    print("outer")

print("line 4")
print("line 5")
print("line 6")
print("END")


# ______________________________________________

# WILL PRINT BOTH EXCEPTION FOR EACH ERRORS
try:

    try:
        print(10 / 0)
    except Exception:
        print("Inner block")
    print(10 / 0)

except Exception as refvar:
    print("outer block")


