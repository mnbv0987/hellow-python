#Program to demonstrate creating and importing Python modules and packages
# importing the library and module
import math
from math import pow
# using the pow()
function pow(3, 5)
print(pow)


# importing the particular function from library
from numpy.linalg import inv
mat = [[12,42,12],[42,10,94],[89,32,34]]
print(inv(mat))

import random
print ("The random number from list is : ",end="")
print (random.choice([50, 41, 84, 40, 31]))

from SubFolder import SubFile as sf
from SubFolder.Beta import Beta
obj = sf.SubFile()
obj.outModels()
obj1 = Beta.Beta()
obj1.outModels()
