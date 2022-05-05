#loop control instruction
Numbers = [6,3,5,7,12,65]
sum = 0
for val in Numbers:
    sum += val
print("The sum is",sum) 


count =0
while count < 5:
    print(count," is less than 5")
    count = count + 1
else:
   print(count," is not less than 5")


list = [1,2,3,4,5,6,7,8,9,10]
n = 5
print("n*i:")
for i in list:
    c = n*i
    print(c, end=" ")



n = int(input("\nEnter the number "))
for i in range(1,11):
    c = n*i
    print(n,"*",i,"=",c)


for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end=" ")


    



    
