nums = [0,1,2,3,4]
index = [0,1,2,2,1]
mylist = []

#solution 1 with insert
for i in range(len(nums)):
    mylist.insert(index[i],nums[i])
print(mylist)

#solution 2 with zip
for ind, num in zip(index, nums):
    mylist.insert(ind, num)
print(mylist)

#solution with slicing
for i in range(len(nums)):
    mylist = mylist[:index[i]] + [nums[i]] + mylist[index[i]:]
print(mylist)
