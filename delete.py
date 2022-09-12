# class Student:
#     marks = 100
#
#     def __init__(self):
#         print(self.marks, id(self.marks))
#         self.marks = 150
#         print("object", self.marks, id(self.marks))
#
#
#
#
# print(Student.marks, id(Student.marks))
#
# obj = Student()
#
# print(Student.marks, id(Student.marks))

class Camera:
    def __init__(self,mp,ss,typ):
        self.mp = mp
        self.ss = ss
        self.typ = typ

class Hp:
    def __init__(self,ram,hdd,pro):
        self.ram = ram
        self.hdd = hdd
        self.pro = pro
        self.add_cam()

    def add_cam(self):
        self.Camera(40,100,"Wide")

class Lenovo:
    def __init__(self,ram,hdd,pro):
        self.ram = ram
        self.hdd = hdd
        self.pro = pro
        self.add_cam()

    def add_cam(self):
        self.Camera(40,100,"Wide")

ob = Hp(4 ,  5)
