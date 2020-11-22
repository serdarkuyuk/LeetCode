nums = [-3,2,-3,4,2]

prefixSum, minimum = 0, float("inf")

for num in nums:
    prefixSum += num
    minimum = min(prefixSum, minimum)

return max(1-minimum, 1)

# mylist = [nums[0]]
# i = 1
# while i < len(nums):
#     mylist.append(mylist[i-1] + nums[i])
#     i += 1
