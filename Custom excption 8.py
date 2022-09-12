age = int(input("Enter age:"))


class AgeLimitExceedError(BaseException):
    def __init__(self, errormsg):
        print(errormsg)


if age > 28:
    raise AgeLimitExceedError("You have exceeded age limit")
else:
    print(" appear for exam")

# now this is complete program for custom exception
