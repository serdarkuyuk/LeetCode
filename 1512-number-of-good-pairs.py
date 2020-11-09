
# nums = [1,2,3,1,1,3]
# nums = []
nums = [1,1,1,1]
myDict = {}
for num in nums:
    if num not in myDict:
        myDict.setdefault(num, 1)
    else:
        myDict[num] += 1

def findfibonachi(n):
    curr = 0
    for i in range(n):
        curr += i
    return curr

def findeasier(n):
    return n*(n-1)/2

summation = 0
for values in myDict.values():
    if values > 1:
        summation += findeasier(values)

print(summation)
