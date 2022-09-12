class Man:
    height = 168.5
    nickname = "striku"
    lucky_number = 9

    def speak(self):
        print("Hi i am a human")

    def shut(self):
        print("i don't wanna talk to you either")

    def tell_height(self):
        print(self.height)



shrikant = Man()
print(shrikant.height)
print(shrikant.nickname)
print(shrikant.lucky_number)
shrikant.speak()
shrikant.shut()
shrikant.tell_height()
