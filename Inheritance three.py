class Parent1:
    def show(self):
        print("Parent 1")

    def parent1Method(self):
        print("Parent 1 method")


class Parent2:
    def show2(self):
        print("Parent 2")

    def parent2Method(self):
        print("Parent 2 method")


class Parent3:
    def show2(self):
        print("Parent 3")

    def parent3Method(self):
        print("Parent 3 method")


class Child(Parent1, Parent2, Parent3):
    pass


childObj = Child()
childObj.show2()
childObj.parent1Method()
childObj.parent2Method()
childObj.parent3Method()

