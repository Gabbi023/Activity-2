f = open("newfile1.txt", "w")
f.write("Python is easy!")

f = open("newfile1.txt", "a")
f.write("\nPython Intermediate")

f = open("newfile1.txt", "r")
print(f.read())
f.close()