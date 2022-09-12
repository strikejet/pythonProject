print("START")
print("line 1")
print("line 2")
print("line 3")

try:
    print(10 / 0)

# exception --> arithmetic exception
except Exception as refvar:
    print(refvar)

print("line 4")
print("line 5")
print("line 6")
print("END")
