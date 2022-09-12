class Parent1:
    def __init__(self, name):
        self.name = name
        print(self.name)


class Child1(Parent1):
    def __init__(self, childname):
        self.childname = childname     # can either use or not use
        super().__init__(childname)


parentobj = Parent1("Manav")
childobj1 = Child1("Yashvi")