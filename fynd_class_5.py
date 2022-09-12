# Function
# function with return type

def display():
    return 100


display()  # returns nothing


# function with print


def add(a, b):
    print(a + b)


add(10, 20)


# function with return


def addi(a, b):
    print()


# function declaration in python


def declfun():
    pass


# default values


def show(a, b, c=100):
    print(a + b + c)


show(10, 20)

show(10, 20, 30)  # will give 60 as answer , overrides the value given in function definition


# Taking multiple inputs with args


def infval(*number):
    print(number)


infval(10, 20, 30, 40)
num1 = int()
print(num1)


# question


def outside(a, b):
    def inside():
        return a * b
    return inside() - 10


print(outside(4, 5))

# accessing global variable with function

shri = 100


def change():
    global shri
    shri = 50


change()
print(shri)   # gives 50


# only last function gets call
def demo():
    print("shri")


def demo():
    print("hi")


def demo():
    print("no")


demo()

