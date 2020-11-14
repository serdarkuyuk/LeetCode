nums = [3,2,2,3]
val = 3

#first solution
i = 0 #first pointer
j = len(nums)-1 #second pointer
while i <= j:
    # find the val from the begining and not val from the end
    #swap them
    if nums[i] == val and nums[j] != val:
        nums[i], nums[j] = nums[j], nums[i]

    #if no val from the begining increase pointer
    elif nums[i] != val:
        i += 1

    #decrease second pointer
    elif nums[j] == val:
        j -= 1

# count how many nan val valuese
count = 0
for num in nums:
    if num != val:
        count += 1
return count

#second solution
i = 0
for num in nums:
    if num != val:
        nums[i] = num
        i += 1
return i
