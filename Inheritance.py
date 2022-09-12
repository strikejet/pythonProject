class Parent:
    def parentMethod(self):
        print("This is parent property")


class Child(Parent):        # this is how you inherit all properties from other class(simple inheritance)
    def childMethod(self):
        print("This is child property")


parentObj = Parent()    # gets only one property
parentObj.parentMethod()

childObj = Child()     # will inherit both properties
childObj.parentMethod()
childObj.childMethod()


# Multilevel inheritance

