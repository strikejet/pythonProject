# why use finally?
# Finally = to close data resources ####
# when there is a work in program that must be done no matter what - like closing data resources
# laptop -- work -- shutdown


# worst case scenario in a program where even exception block creates error

try:
    print("open file")
    print(10 / 0)

except ArithmeticError as refvar:
    print(10 / 0)
    print(refvar)
    print("File read / edit / delete")
    print("save")
    print("close file")

finally:
    print("close file")

