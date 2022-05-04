  

#Program to demonstrate error-handling and multi-threading in Python.
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b;
    print("a/b = %d"%c)
except:
    print("can't divide by zero")
else:
    print("Hi I am else block")
    

try:
    fileptr = open("file2.txt","r")
    try:
        fileptr.write("Hi I am good")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")


import threading
def print_hello(n):
    print("Hello, how old are you? ", n)
T1 = threading.Thread( target = print_hello, args = (20, ))
T1.start()
T1.join()
print("Thank you")


import threading
def print_cube(num):
    print("Cube: {}".format(num * num * num))
def print_square(num):
    print("Square: {}".format(num * num))
if __name__== "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")
