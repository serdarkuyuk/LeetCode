nums = [8,1,2,2,3]

numsSorted = sorted(nums)
myDict = {}

#solution 1
prev = None
count = 0
for i in numsSorted:
    if prev != i:
        myDict[i] = count
        prev = i
    count += 1

myList = [myDict[i] for i in nums]

print(myList)


#solution 2 same more clear
for i, num in enumerate(numsSorted):
    if num not in myDict:
        myDict[num] = i

myList = [myDict[key] for key in nums]

print(myList)
