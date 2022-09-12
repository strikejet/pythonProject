# decorator is used to reduce writing a code again and again


def sub(num1, num2):
    print(num1 - num2)


def changeIt(function):  # decorator
    def inside(num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
            return function(num1, num2)

    return inside


substract = changeIt(sub)
substract(10, 20)


@changeIt  # modularity __ if you want to to use it just use it before function or remove @changeit
def div(num1, num2):
    print(num1 / num2)


div(2, 10)
