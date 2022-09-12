age = int(input("Enter age:"))


class AgeLimitExceedError:
    pass


if age > 28:
    raise AgeLimitExceedError()
else:
    print(" appear for exam")

# will give error that error should be from base exception
# because we haven't derived any properties from exception class
