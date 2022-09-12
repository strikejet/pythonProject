# THis is multiple inheritance
class ParentOne:
    def parentOnemethod(self):
        print("Parent - 1 Method")


class ParentTwo:
    def parentTwomethod(self):
        print("Parent - 2 Method")


class ParentThree:
    def parentThreemethod(self):
        print("Parent - 3 Method")


class Child(ParentOne, ParentTwo, ParentThree):  # Inherits from all three parents can be done only in python
    pass


childObj = Child()
childObj.parentOnemethod()
childObj.parentTwomethod()
childObj.parentThreemethod()


# -------------------------------------------------------------------------
# Problem with multiple inheritance


class Parent1:
    def show(self):
        print("Parent 1")


class Parent2:
    def show(self):
        print("Parent 2")


class Child(Parent1, Parent2):
    pass


childObj = Child()
childObj.show()

# Question is which show property will child inherit ?

# And for this only particular case child will inherit first parent property
# this work as multilevel inheritance
# its similar as tree data structure  it will only take left node of the branch internally
