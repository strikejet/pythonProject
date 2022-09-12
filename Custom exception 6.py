age = int(input("Enter age:"))


class AgeLimitExceedError(ArithmeticError):
    pass


if age > 28:
    raise AgeLimitExceedError()
else:
    print(" appear for exam")

# now we have inherited arithmetic error class for your error
