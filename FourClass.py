# self is taking one argument which is object internally
# So even though we have 3 arguments in method definition one is taken by object
class Calci:

    def addi(self, num1, num2):
        print(num1 + num2)
        print(type(firstset))

    def multi(self, num1, num2):
        return num1 * num2


firstset = Calci()
firstset.addi(8, 9)
result = firstset.multi(8, 9)
print(result)
