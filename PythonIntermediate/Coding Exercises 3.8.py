f = open("newfile.txt", "r")
print(f.read())

f = open("newfile.txt", "r")
print(f.readline())

f = open("newfile.txt", "r")
for x in f:
    print(x)
f.close()

import os

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("The file does not exist")