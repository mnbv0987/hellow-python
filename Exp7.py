class car:
    def __init__(self,modelname, year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,self.year)
c1 = car("Toyota", 2016)
c1.display()


class Employee:
    id = 10
    name = "John"
    def display (self):
        print("ID: %d \nName: %s"%(self.id,self.name))
emp = Employee()
emp.display()


class Student:
    count = 0
    def __init__(self):
        Student.count = Student.count + 1
s1=Student()
s2=Student()
print("The number of students:",Student.count)


class Student:
    def __init__(self):
        print("The First Constructor")
    def __init__(self):
        print("The second contructor")
st = Student() 
