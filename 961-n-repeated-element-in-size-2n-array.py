A = [2,1,2,5,3,2]
#hashmap solution
myDict = {}
for key in A:
    if key not in myDict:
        myDict[key] = 1
    else:
        return (key)


#set solution
mySet = set()
for key in A:
    if key not in mySet:
        mySet.add(key)
    else:
        return (key)
# print("$$$$$$$$")
# print(A.count(2))
