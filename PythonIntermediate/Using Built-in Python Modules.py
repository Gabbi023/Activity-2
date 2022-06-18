#built-in modules
help("modules")
help("random")

print(dir("random"))

#random module
from random import randint

print(int(randint(1,1000)))

#datetime module

import datetime

t = datetime.datetime.now()

print(t)

import datetime

t = datetime.datetime(2022, 6, 18)

print(t.strftime("%B"))
print(t.year)
