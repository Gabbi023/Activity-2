class Pets:
    looks = "Adorable!"

hamster = Pets()

print(hamster.looks)


class Guest:
    pass

g_1 = Guest()

g_1.first = "Eve"
g_1.last = "Dela Cruz"
g_1.interest = "Anime"
g_1.phone = 12345

print(g_1.interest)

g_2 = Guest()

g_2.first = "Adam"
g_2.last = "Perez"
g_2.interest = "Russian Literature"
g_2.phone = 87654

print(g_2.phone)
