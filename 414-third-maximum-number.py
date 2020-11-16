# nums = [2, 2, 3, 13, 13, 50, 7, 1, 6, 10]
arr = [1,2,2,5,3,5]
nums, mylist = list(set(nums)), [float("-inf")]*3

for i in range(len(nums)):
    if nums[i] > mylist[0]:
        mylist = [nums[i], mylist[0], mylist[1]]
        continue
    elif nums[i] > mylist[1]:
        mylist = [mylist[0], nums[i], mylist[1]]
        continue
    elif nums[i] > mylist[2]:
        mylist = [mylist[0], mylist[1], nums[i]]

return mylist[2] if mylist[2] != float("-inf") else mylist[0]

print(mylist)
