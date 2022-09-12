# this quite different from other programming languages so need to understand the differences
# Abstraction - Hiding details , displaying only interface (client can only view certain things)

# ways to import functions or methods from other file
# import fynd_class_5
# fynd_class_5.display()   # will import all functions so not as much efficient

# from fynd_class_5 import display, add
# display()
# add(5, 6)

# in java<> 1 .  abstract class 2. abstract class--> object creation is not allowed from abstract class 3. But you
# can inherit abstract class 4. Abstract method __> method declaration _> can only be declared in abstract class 5.
# abstract class --> which contains abstract method--> it is mandatory for inherited class to provide body for the
# abstract method
# ABC -  abstract class


from abc import ABC, abstractmethod


class Abs(ABC):
    def methodwithbody(self):
        print("this is method with body inside abstract class")

    @abstractmethod
    def absmethod(self):
        pass


# obj = Abs()      # we have created a object from abstract class which cannot be done in other languages
# obj.methodwithbody()
# obj.absmethod()


class InheritAbsClass(Abs):
    def absmethod(self):
        print("I have implemented abstract method here")


obj = InheritAbsClass()   # this gives wrong error message -
# error - Can't instantiate abstract class InheritAbsClass with abstract methods absmethod
# actual error - you have to provide body for abstract method if you are inheriting from abstract class

obj.absmethod()
obj.methodwithbody()
