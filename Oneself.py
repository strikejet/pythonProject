# initialise a value from and object


class Emp:
    def mymethod(self):
        print(" This is instance method")

    def __init__(self):
        print("This is constructor")


e1 = Emp()
e2 = Emp()
e1.mymethod()
Emp()    # an object is made here just not assigned it to any reference variable
# do we need to call constructor --> No (It will be autocalled at time of object initialisation)
#  __init__ is no return type - > constructor is made to just initialise so there is no return type

print(type(Emp))
