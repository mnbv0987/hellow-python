#Program to demonstrate file-handling in Python.
fileptr = open("file.txt","r")
if fileptr:
    print("file is opened successfully")
fileptr.close()


with open("file.txt",'r') as f:
    content = f.read()
    print(content)

    
fileptr = open("file2.txt","w")
fileptr.write(" Python has an easy syntax and user-friendly interaction.")
print("file wrote successful…")
fileptr.close()


fileptr = open("file.txt","r");
content = fileptr.readlines()
print(content)
fileptr.close()


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("demofile3.txt", "r")
print(f.read())
