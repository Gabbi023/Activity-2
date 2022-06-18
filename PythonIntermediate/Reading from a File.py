f = open("new.txt", "r")
print(f.read())

#return characters

f = open("new.txt", "r")
print(f.read(12))

f = open("new.txt", "r")
print(f.readline())
print(f.readline())

f = open("new.txt", "r")
for x in f:
    print(x)

f.close()

#delete file

import os

if os.path.exists("newfile1.txt"):
    os.remove("newfile1.txt")
else:
    print("The file does not exist")