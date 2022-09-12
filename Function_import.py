def show():
    print("show")


def display():
    return 100


class Home:
    def area(self):
        print("my area is this")


number = 200

# __name__   --> fixed variable name
# __main__  ---> value __.> current file
# we use following code to not call the functions when we import the functions
# from this file to another file
# these function call will not auto execute if any function is imported to other file now

if __name__ == "__main__":
    show()
    print(display())
    print(number)

