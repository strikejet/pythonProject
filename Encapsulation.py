# security
# user defined data type
# access speci / modi ----> public, private, protected

# by default ----> public ----> each and every classes , packages
# _  ---> protected   ---> derived classes , own class
# __ ---> Private     --- own class


class Parent:
    value = 100             # public
    _name = "python"        # protected
    __fval = 4.5            # private

    def show (self):
        print("behv")

    def display(self):
        print(self.__fval)


class Child(Parent):
    def show(self):
        print(self.__fval)


p1 = Parent()
c1 = Child()


print(p1.value)
print(c1.value)

print(p1._name)
print(c1._name)

# print(p1.__fval)    # will not work
# print(c1.__fval)    # will not work

p1.display()
# c1.__fval()         # will not work
# c1.show()           # will not work
