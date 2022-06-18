f = open("new.txt", "w")
f.write("I like Python because it's easy to understand")

f = open("new.txt", "a")
f.write("\nI plan to create apps")

f = open("new.txt", "a")
f.write("\nUse it on the apps I plan to create")

f = open("new.txt", "a")
f.write("\nI want to be a Game Developer")

f = open("new.txt", "r")
print(f.read())
f.close()