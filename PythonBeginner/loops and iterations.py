colors = ["purple", "red", "orange", "yellow"]
for x in colors:
    print(x)

for x in "orange":
    print(x)

colors = ["purple", "red", "orange", "yellow"]
for x in colors:
    if x  == "red":
        continue
    print(x)


colors = ["purple", "red", "orange", "yellow"]
for x in colors:
    print(x)
    if x == "red":
        break



x = range(8)
for y in x:
    print(y)


colors = ["purple", "red", "orange", "yellow"]

things = ["car", "notebook", "shirt", "shoes"]

for x in colors:
    for y in things:
        print(x, y)

i = 1
while i <= 10:
    print(i)
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i)

i = 1
while i < 7:
    print(i)
    i += 1
else:
    print("i is no longer less than 7.")