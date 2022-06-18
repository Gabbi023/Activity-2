employee_1 = {"Name": "Frank", "Position": "Sales Representative", "Email Address": "frank@company.com"}

for key, value in employee_1.items():
    print(key)
    print(value)

characters_weapons ={"Harry Potter": "wand", "Percy Jackson": "riptide", "Katniss Everdeen": "bow and arrow",
                     "Bilbo Baggins": "Ring"}

for name in characters_weapons.keys():
    print(name)

for name in characters_weapons.keys():
    if name == "Percy Jackson":
        continue
    print(name)


most_delicious = {"McDonald's": ["fried chicken", "sundae"], "Jollibee": ["fried chicken", "spaghetti"],
                  "KFC": ["gravy", "mashed potatoes"], "Pizza Hut": ["pizza", "pasta"]}

for item in most_delicious.values():
    print(item)

#nested keyword

cat = {1: {"name": "Sweetie", "age": "12", "color": "white"},
       2: {"name": "Ethel", "age": "3", "color": "orange"}}

print(cat)
print(cat[2]["age"])
print(cat[1]["name"])
print(cat[2]["color"])

cat[3] = {}
cat[3]["name"] = "Tuna"
cat[3]["age"] = "5"
cat[3]["color"] = "black"
cat[3]["personality"] = "friendly"

print(cat[1])
print(cat[2])
print(cat[3])

cat[4] = {"name": "Bubbles", "age": "7", "color": "gray", "personality": "grumpy"}

print(cat[1])
print(cat[2])
print(cat[3])
print(cat[4])