class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("(parent class/User) Username:", self.username, "password:", self.password)

class Admin(User):
    def display2(self):
        print("(subclass/Admin) Username:", self.username, "password:", self.password)

a_1 = Admin("leslie2001", "password1234")
u_45 = User("pretty_jun25", "otherpassword287")

u_45.display1()
a_1.display2()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("Parent Class/User")
        print("Username:", self.username)
        print("password:", self.password)

class Admin(User):
    def __init__(self, username, password, code):
        self.code = code
        User.__init__(self, username, password)

    def display3(self):
        print("Subclass/Admin")
        print("Username:", self.username)
        print("Password:", self.password)
        print("code:", self.code)

u_45 = User("pretty_jun25", "otherpassword287")
a_1 = Admin("leslie2001", "password1234", "2468")

u_45.display1()
a_1.display3()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display1(self):
        print("Username:", self.username)
        print("password:", self.password)

class Admin(User):
    def __init__(self, username, password, code):
        self.code = code
        super().__init__(username, password)

    def display3(self):
        super().display1()
        print("code:", self.code)

a_1 = Admin("leslie2001", "password1234", "2468")
a_1.display3()