# why use finally?
# Finally = to close data resources ####
# when there is a work in program that must be done no matter what - like closing data resources


# program terminates but finally is executed

print("START")
print("line 1")
print("line 2")
print("line 3")

try:
    print(20 / 0)


finally:
    print("Always executed")

print("line 5")
print("end")
