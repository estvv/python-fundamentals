from math import cos # import cos from the math library
from math import * # import all the func from the math library

print(cos(90))
print(sin(90))

####################################################
print("-------------------------------------------")
####################################################

from random import randint

nombre = randint(0, 10)
print(nombre)

for i in range(0, 10):
    print(str(randint(-10, 10)) + " ", end='')
print("")

####################################################
print("-------------------------------------------")
####################################################

import os

os.system("echo HelloWorld")
#os.system("curl parrot.live")