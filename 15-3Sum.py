nums = [-1, 0, 1, 2, -1, -4]
length = len(nums)
if length < 3:
    print([])  # return []
nums.sort()
result = []
i = 0
for i in range(length-2):
    if nums[i] > 0:
        break
    if i == 0 or nums[i] != nums[i-1]:
        low, high = i+1, length-1
        while low < high:
            summation = nums[i] + nums[low] + nums[high]
            if summation == 0:
                result.append([nums[i], nums[low], nums[high]])
                while low < high and nums[low] == nums[low+1]:
                    low += 1
                while low < high and nums[high] == nums[high-1]:
                    high -= 1
                low, high = low+1, high-1
            elif summation < 0:
                low += 1
            else:
                high -= 1
print(result)
