class Parent:
    def __init__(self):
        print("parent")


class Child(Parent):
    def __init__(self):
        print("child")


c1 = Child()

# will only get child because "INIT" is  not a constructor only a method
# In other languages it will first take constructor from parent and then child