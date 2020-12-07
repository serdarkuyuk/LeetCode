nums = [0,1,0,3,12]
# nums = [1,0,1]

tail = 0
for fast in range(len(nums)):
    if nums[fast] != 0:
        nums[tail], nums[fast] = nums[fast], nums[tail]
        tail += 1
print(nums)
def funct(x):
    pass
