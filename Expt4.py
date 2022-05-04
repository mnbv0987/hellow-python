#list,touple,dictionaries
List = [1, 2, 3, 4, 5]
List1 = [i for i in range(5)]
print(List1)


list2 = [1, 2, 3, 4, 5]
list2.remove(4)
print(list2)
L1 = ['a', 'b']
L2 = ['c', 'd']
L1.extend(L2)
print(L1)

list3 = ["Apple", "Mango", "Banana"]
print(list3.insert(0, 33))
print(list3.insert(6, 29))
print(list3)


tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3)



tuple1 = ('xyz', 'zara', 'abc'),
tuple2 = (456, 700, 200)
print("Max value element : ", len(tuple1))
print("Max value element : ", max(tuple2))


dict1 = {"Brand": "gucci", "Industry": "fashion", "year": 1921}
print(dict1)
dict1['product'] = "Tote Handbag"
print(dict1)

cubes = {1: 1, 2: 8, 3: 21, 4: 64, 5: 125}
print(cubes.pop(4))
print(cubes)

order = {'coffee': 43, 'tea': 67, 'biscuit': 51, 'croissants': 83}
s_order = sorted(order.items(), key=lambda x: x[1], reverse=True)
for i in s_order:
    print(i[0], i[1])
 
