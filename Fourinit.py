#    def __init__(self, id):
#       empid = id      (Without self initialisation can't be done)

class Emp:
    def __init__(self, id):
        self.empid = id


nikunj = Emp(100)
sachin = Emp(200)

print(nikunj.empid)
print(sachin.empid)