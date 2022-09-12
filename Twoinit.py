class Emp:
    def mymethod(self, number1):
        print("this is instance method - ",number1)

    def __init__(self):
        print("This is constructor")


nikunj = Emp()
sachin = Emp()
print(id(Emp()))

# sachin.mymethod(100)

print(id(nikunj))
print(id(sachin))

manav = Emp
print(id(Emp))
print(id(manav))

m1 = manav()
m1.mymethod(7)