#inheritance, overriding, and MRO in Python
class FirstClass:
    def course(self):
        print("Python tutorial")
class hello(FirstClass):
    def func(self):
        print("Welcome to Python World..")
ob1 = hello()
ob1.func()
ob1.course()


class Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))

class Animal:
    def speak(self):
        print("speaking")
class Dog(Animal):
    def speak(self):
        print("Barking")
d = Dog()
print("overriding:")
d.speak()


class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
class C(A):
    def rk(self):
        print("In class C")
class D(B, C):
    pass
r = D()
print("MRO IN PYTHON:")
r.rk()
