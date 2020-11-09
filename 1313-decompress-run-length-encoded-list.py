# nums = [1,2,3,4]
nums = [1,1,2,3]*100

myList = []
for i in range(0, len(nums), 2):
    myList.extend([nums[i+1]]*nums[i])
print(myList)
