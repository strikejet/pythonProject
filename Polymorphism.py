# polymorphism
# one entity performs different tasks in different scenarios
# method overloading --> one class --> two methods with same name but different count parameter
# (or) one class --> two methods with same name with same count of parameter but different type of parameters
# we don't have method overloading concept in python
# Method overriding --> two classes --> one method with same name and same count of parameter with inheritance


class Calc:
    def add(self, num1, num2, num3):
        print(num1 + num2 + num3)

    def add(self, num1, num2):
        print(num1 + num2)  # we don't have methods in python only references so python just references second add function and overrides first one

obj = Calc()
# obj.add(10, 20, 30) # gives error because python will refer to second add function

# ---------------------------------------------------------------------------------------

#  method overriding
# we are overriding the method defined in parent class in the child class. When we call that method through object of
#  child class function that is defined in child class is

class Emp:
    def aboutEmp(self, name):
        print("This is Emp name")


class NewEmp(Emp):
    def aboutEmp(self, myName):
        print("This is empname and sname")


obj = NewEmp()
obj.aboutEmp("Manav")


# -----------------------------------------------------

# operator overloading

# Dunder Methods
# Operator methods

class Clac:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):                    # __add__ is binded to + operator
        return self.value + other.value

    def __mul__(self, other):                     # __mul__ is binded to * operator
        return self.value / other.value


num1 = Clac(20)
num2 = Clac(50)

print(num1.value + num2.value)
print(num1 + num2)          # will not work without ddefining __add__ method
print(num1*num2)   # gives division even if * is used because we defined * logic as division

# ------------------------------------------------------------------------------

# Duck typing -- > accessing method of a class from object to determine whether object belongs to that class or not


class Human:
    def thinks(self):
        print("Belongs to human class")


class Alien:
    def supernatural(self):
        print("Belongs to alien class")


class Animal:
    def loves(self):
        print("Belongs to animal class")


def checkbehaviour(self):
    self.supernatural()
    self.loves()
    self.thinks()


manav = Human()
jadu = Alien()
simba = Animal()

checkbehaviour(manav)
