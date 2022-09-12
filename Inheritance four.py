# What if you want to invoke parent methods from child class?
# we use "super()" to access parent class method in child class (can only be used in child class )
# we may be able to do the same with "self" but that's calling from ch1 object and not from child class
# class Parent:
#
#     name = "shrikant"
#
#     def parentM(self):
#         print("This parent prop")
#
#
# class Child(Parent):
#     def childM(self):
#        self.parentM()
#        print(self.name)
#        print("This is child prop")


class Parent:

    name = "shrikant"

    def parentM(self):
        print("This parent prop")


class Child(Parent):
    def childM(self):
        super().parentM()
        print(super().name)
        print("This is child prop")


ch1 = Child()
ch1.childM()
