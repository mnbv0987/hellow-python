#array using numpy,function and anonymous fuction
import numpy as np
arr = np.empty((3,2), dtype = int)
print(arr)

import numpy as np
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])
print("Printing array:")
print(a);
print("Iterating over the array:")
for x in np.nditer(a):
    print(x,end=' ')
 
import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[12,30]])
z=np.concatenate((x,y))
print(z)
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2, li))
print(final_list)
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function = ",list1)
list1 = [10,30,40,50]
change_list(list1)
print("list outside function = ",list1)

def para_func(name,age=22):
    print("My name is",name,"and age is",age)
para_func(name = "john")
para_func(age = 10,name="David")
