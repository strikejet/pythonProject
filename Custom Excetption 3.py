age = int(input("Enter age:"))

# raise
# compile time error

if age > 28:
    raise(" can't appear for exam")
    print(" use backend to appear for exam")   # this is error won't be executed

else:
    print(" appear for exam")