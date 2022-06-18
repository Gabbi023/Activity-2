shopping_list = {"weird hat": 150, "purple rug": 450, "old books": 200, "stuffed elephant": 50}

print(shopping_list)


basketball_teams = {"Crouching Tigers": ["Jacob", "Kevin", "Roni", "Joshua", "Isagani"],
                    "Hidden Dragons": ["Ted", "Bryan", "Edu", "Luis", "Mark"]}

print(basketball_teams)


anime_characters = {"Name": "Eren", "Age": 19, "Childhood Friends": ["Armin", "Mikasa"]}

print(anime_characters)


shopping_list = {"weird hat": 150, "purple rug": 450, "old books": 200, "stuffed elephant": 50}

shopping_list["plastic ring"] = 20

print(shopping_list)

shopping_list = {"weird hat": 150, "purple rug": 450, "old books": 200, "stuffed elephant": 50}

shopping_list["purple rug"] = 500
print(shopping_list)

pets = {"Gerald": "guinea pig", "Alice": "dog", "Ruby": "cat"}

pets.update({"Ron": "gecko", "Paulina": "hamster", "Marlon": "goldfish"})

print(pets)

relative = ["Tita Malou", "Jeff", "Tito Roger", "Veronica"]

age = [54, 14, 55, 19]

combined_lists = zip(relative, age)

print(list(combined_lists))


relative = ["Tita Malou", "Jeff", "Tito Roger", "Veronica"]

age = [54, 14, 55, 19]

relative_age = dict(zip(relative, age))

print(relative_age)