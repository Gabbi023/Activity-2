import module1

module1.greeting("Gabbi")

a = module1.user_1

print("Hey there, " + a.name + "! Ready to do some math?")

c = module1.user_3

print("Hey there, " + c.name + "! Ready to do some math?")


#Renaming Modules

import module1 as m1

m1.greeting("Gabbi")

a = m1.user_1

print("Hey there, " + a.name + "! Ready to do some math?")

c = m1.user_3

print("Hey there, " + c.name + "! Ready to do some math?")

import module1

sum = module1.get_sum(4591, 782)
print(sum)

quotient = module1.get_quo(100, 22)
print(quotient)

#from keyword
from module1 import *

product =  get_prod(9, 4)
print(product)