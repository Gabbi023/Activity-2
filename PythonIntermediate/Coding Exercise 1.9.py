class ClubMembers:
    def __init__(self, name, birthday, age, favoritefood, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favoritefood = favoritefood
        self.goal = goal

    def display1(self):
        print("Name:", self.name)
        print("birthday:", self.birthday)
        print("age:", self.age)
        print("favorite food:", self.favoritefood)
        print("goal:", self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favoritefood, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favoritefood, goal)
    def display2(self):
        print("Name:", self.name)
        print("birthday:", self.birthday)
        print("age:", self.age)
        print("favorite food:", self.favoritefood)
        print("goal:", self.goal)
        print("position:", self.position)

m_1 = ClubMembers("Tom", "January 16", "14", "Ice cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", "16", "Beef stronganoff", "To be the world's greatest chef", "Treasurer")

m_1.display1()
o_4.display2()

