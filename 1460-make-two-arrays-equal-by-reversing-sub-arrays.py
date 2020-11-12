# target = [1,2,3,4]
# arr = [2,4,1,3]
target = [1,2,2,3]
arr =[1,1,2,3]

#solution 1
from collections import Counter
arrDict = Counter(arr)
targetDict = Counter(target)
print(arrDict == targetDict)


#solution 2
arrDict = {}
targetDict = {}

for i in target:
    targetDict[i] = targetDict.get(i, 0) + 1
for j in arr:
    arrDict[j] = arrDict.get(j, 0) + 1

print(targetDict, arrDict)
