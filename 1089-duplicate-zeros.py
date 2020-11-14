arr = [1,0,2,3,0,4,5,0]
# nums = [1,2,3]
# i = 0
# while i < len(nums):
#     if nums[i] == 0:
#         nums.insert(i+1, 0)
#         nums.pop()
#         i += 2
#     else:
#         i += 1
# print(nums)

#O(n) solution
zeroes = arr.count(0)
print(zeroes)
n = len(arr)
for i in range(n-1, -1, -1):
    print(i,zeroes, i+zeroes,arr)
    if i + zeroes < n:
        arr[i + zeroes] = arr[i]
    if arr[i] == 0:
        zeroes -= 1
        if i + zeroes < n:
            arr[i + zeroes] = 0
print(arr)
