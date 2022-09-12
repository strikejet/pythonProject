# empid can be printed if we just need it to be executed but we can't execute it while assigning it to an object
# because without self we can't create attribute of cartain object inside init constructor

class Emp:
    def __init__(self, id):
        empid = id
        print(empid)


nikunj = Emp(100)
sachin = Emp(200)

# print(nikunj.empid)    Not working due to object attribute accession without self
