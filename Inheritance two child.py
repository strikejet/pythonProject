class Parent:
    def parentmethod(self):
        print("This is parent method")


class Child1(Parent):
    def child1method(self):
        print("This is first child method")


class Child2(Parent):
    def child2method(self):
        print("this is second child method")


c1 = Child1()
c2 = Child2()

c1.parentmethod()      # both inherit from parent class
c2.parentmethod()

c1.child1method()       # but they can not inherit from other child class
c2.child2method()
