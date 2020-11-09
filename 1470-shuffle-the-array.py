nums = [2,5,1,3,4,7]
n = 3
mylist = []

#1st solution with append
for i in range(n):
    mylist.append(nums[i])
    mylist.append(nums[n+i])

#2nd solution with extend
for i in range(n):
    mylist.extend([nums[i],nums[n+i]])

#3th solution with zip
for i,j in zip(nums[:n], nums[n:]):
    mylist.extend([i,j])
return mylist

#4th soution with generator
def myGenerator(nums, n):
    for i in range(n):
        yield nums[i]
        yield nums[i+n]

generator = myGenerator(nums, n)
for _ in range(n*2):
    print(next(generator))
