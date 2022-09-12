# file -- it contains data -- type -- .csv
# file handling -- performing tasks on file
# _------- open , read, write , close, append

myfile = open("mydata.txt", "r")
# print(myfile) # will not work
# print(myfile.read())

# will take lines one by one consecutively
# print(myfile.readline())  # first line
# print(myfile.readline())   # second line
# print(myfile.readline())    # third line
# print(myfile.readline())     # fourth line

# returns object in form of list
# print(myfile.readlines())

# for data in myfile:
#   print(data)

# print(myfile.read(2))
# print(myfile.readline(4))


# print(myfile.readlines(2))
# print(myfile.readlines(6))

# myfile = open("mydata.txt", "w")
# myfile.write("This is new data")
# myfile.writelines(["one\n","two\n","three"])
# myfile = open("myDataNewFile.txt","w")
# myfile.write("This is new fie")

# myfile = open("mydata.txt", "a")
# myfile.write("\nNew Data")


# setting pointer
# myfile = open("mydata.txt", "r")
# print(myfile.read())
# print(myfile.read())    # will only read one time because pointer has passed
# print(myfile.tell())      # will tell you pointer location
# print(myfile.seek(19))   # will get pointer to given location # printing for clarification
# print(myfile.read())
# print(myfile.tell())


# myfile = open("mydata.txt", "r")
# print(myfile.read())
# myfile.close()
# print(myfile.read())

# with open ("mydata.txt", 'r') as myfile:
#     print(myfile.read())             # will close automatically after intendation
# it has scope like for loop and functions
# print(myfile.read())  # will get error as it is outside scope of "with"

#  -------------------------------------------------------------------------

# encoding

mynotebook = range(0, 10)

# with open("binfile", "bw") as binaryfile:    # bw - creates write file in binary
#   ( binaryfile.write(mynotebook)   )   # won't work because binary requires byte type data not range
#   binaryfile.write(bytes(mynotebook))  # will work

with open("binfile", 'br') as readbinaryfile:
    print(readbinaryfile.read())

# --------------------

# homework   _-__ learn about pickle model
