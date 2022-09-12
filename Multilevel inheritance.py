# Multilevel inheritance

class Parent:
    def parentmethod(self):
        print("This is parent method")


class Child(Parent):
    def childmethod(self):
        print("This is child method")


class Grandchild(Child):      # inherits from child and thus from parent as well
    def grandchildmethod(self):
        print("this is grandchild method")


t1 = Grandchild()
t1.parentmethod()    # this accesses parent method as well as child method
t1.grandchildmethod()
t1.childmethod()
