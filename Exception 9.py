# try  -- except -- finally
# try needs at least one exception or maximum one finally
# try -- more except
# try -- except -- finally
# if you only use try and finally and error is not handled - program terminates after performing finally
# even if error occurs or not finally gets executed

print("START")
print("line 1")
print("line 2")
print("line 3")

try:
    print(10 / 0)

except ArithmeticError as refvar:
    print(refvar)
    print("block")

finally:
    print("always executed")
