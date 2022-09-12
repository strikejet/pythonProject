# Error  --> runtime and compile time  --> Handle possible but not supposed to handle it
# Exception --> syntax --> correct    logic --> incorrect
# exception  -- > runtime , compile time __> Handle possible and supposed to handle it
# runtime --> Unchecked exception
# compile time --> checked exception

# exception handling --> so program does not terminate and we give proper message on client side
# try:    except:
# except  --> Print messages to user
# except --> replace coding
# try --> will need atleast one except or one finally

print("START")
print("line 1")
print("line 2")
print("line 3")
nume = int(input("Numerator:"))
deno = int(input("Denominator:"))
# these should be coded outside try because they have to global or cannot be used by except part
try:
    print(nume / "str")

# except should not be used bare
# we need to specify which error is estimated so the following solution is aplied
# Exception  --> this keyword is " all in one exception "for all errors
except ArithmeticError:
    print("Specific doctor")
    print("denominator cannot be zero")

print("line 4")
print("line 5")
print("line 6")
print("END")





nume = int(input("Numerator:"))
deno = int(input("Denominator:"))
try:
    print(nume / deno)

# here when we use except Arithmetic error we already create a object fromm arithmetic error class
# now we can provide reference variable to that object so we can access it
except ArithmeticError as refvar:
    print(ArithmeticError)
    print(refvar)
    print(id(refvar))
    print("Specific doctor")
    print("denominator cannot be zero")

# Exception class is parent class to all other exception classes


