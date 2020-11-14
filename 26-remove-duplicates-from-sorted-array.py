nums = [0,0,1,1,1,2,2,3,3,4]
# length = len(nums)
# i=0
# while i < length-1 :
#     if nums[i] == nums[i+1]:
#         nums.remove(nums[i])
#         length -= 1
#     else:
#         i +=1
# print(nums)
#
# nums = [0,0,1,1,1,2,2,3,3,4]
# x = 1
# for i in range(len(nums)-1):
#     if nums[i] != nums[i+1]:
#         x += 1
# print(x)



tail = 0
for fast in range(1,len(nums)):
    if nums[tail] != nums[fast]:
        tail += 1
        print(tail,nums[tail], nums[fast])
        nums[tail] = nums[fast]
print(nums,tail+1)
