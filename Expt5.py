#string,set and array
str1 = 'Hello Python'
print(str1)
str2 = "Hello Python"
print(str2)
str3 = '''''Triple quotes are generally used for represent the multiline or
docstring'''
print(str3)
 
str = "this is string example.	wow!!!"
print("str.center(40, 'a') : ", str.center(40, 'a'))
str = "THIS IS STRING EXAMPLE.	WOW!!!";
print(str.isupper())
str = "THIS is string example.	wow!!!";
print(str.isupper())


myset = {"apple", "banana", "cherry"}
myset.update(["orange", "mango", "grapes"])
print(myset)

Set_A = {1,2,3,4,5}
Set_B = {4,5,6,7}
print(Set_A | Set_B)

#Set_A = {1,2,3,4,5}
#Set_B = {4,5,6,7}
#ptint (Set_A & Set_B)

myset1 = {"apple", "banana", "cherry"}		
x = myset1.pop()		
print("Popped element:",x,myset1)

import array as arr		
a = arr.array('i', [2,4,6,8])		
print(a)

Student_marks = [[96, 91, 70, 78, 97],	[80, 87, 65, 89, 85],[90, 93, 91, 90, 94], [57, 89, 82, 69, 60],[72, 85, 87, 90, 69]]		
print(Student_marks[1])		
print(Student_marks[0])		
print(Student_marks[2])		
print(Student_marks[3][4])		
arr = [1, 2, 3, 4, 5]
print("The array is:", arr)
arr2 = arr[: : -1]
print("The Array in reversed order:", arr2)
