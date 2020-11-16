# nums = [4,3,10,9,8]
# nums = [4,4,7,6,7]
nums = [6]
nums.sort(reverse=True)
print(nums)


i, j = 0, len(nums)-1
lefttotal = nums[0]
rightotal = nums[-1]
while i < j:
    print(lefttotal, i ,rightotal, j)
    if lefttotal > rightotal:
        j -= 1
        rightotal += nums[j]

    else:
        i += 1
        lefttotal += nums[i]
print(nums[:i+1])
