# question - invoke parent class method from object class


class Parent:
    def __init__(self, Id):
        self.Id = Id

    def show(self):
        print("Id in parent:", self.Id)


class Child(Parent):
    def __init__(self, Id):
        self.Id = Id
        super().__init__(Id)

    def display(self):
        super().show()
        print("Id in child:", self.Id)


parentobj = Parent(20)
parentobj.show()
childObj = Child(10)
childObj.display()

# ---------------------------------------------------------------------------


class Parent1:
    def __init__(self, name):
        self.name = name
        print(self.name)


class Child1(Parent1):
    def __init__(self, childname):
        # self.childname = childname     can either use or not use
        super().__init__(childname)


parentobj = Parent1("Manav")
childobj1 = Child1("Yashvi")
