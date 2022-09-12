age = int(input("Enter age:"))

if age > 28:
    raise ArithmeticError(" can't appear for exam")
else:
    print(" appear for exam")

    # we are stopping program now but still its giving an error which may not be understood by user