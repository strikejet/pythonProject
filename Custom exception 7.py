age = int(input("Enter age:"))


class AgeLimitExceedError(BaseException):
    pass


if age > 28:
    raise AgeLimitExceedError()
else:
    print(" appear for exam")

    # still we need to give proper message for user