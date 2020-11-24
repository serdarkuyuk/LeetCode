nums = [3,4,2,3]
nums = [4,2,1]
nums = [-1,4,2,3]
nums = [1,1,1]
       #4 2 3
counter = None
i = 0
while i in range(len(nums)-1):

    if nums[i] > nums[i+1] :
        if counter is not None:
            print(False)
            break
        counter = i
    i += 1
print(counter == None or counter == 0 or counter == len(nums)-2 or nums[counter-1] <= nums[counter+1])
