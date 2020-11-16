nums =[4,3,2,7,8,2,3,1]

for i in range(1, len(nums)+1):
    print(i)

    nums[abs(i)-1] = -1 * nums[abs(i)-1]

print(nums)
