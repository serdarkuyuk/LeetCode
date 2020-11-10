left = 1
right = 22
#solution 1
mylist = []
while left <= right:
    num = left
    flag = 0
    while num:
        num, digit = divmod(num, 10)
        if digit != 0 and left % digit == 0:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        mylist.append(left)
    left += 1
print(mylist)



#solution 2
nums = []
for num in range(left, right+1):
    num_ = num
    while num_ > 0:
        num_, rem = divmod(num_, 10)
        if rem == 0 or num % rem != 0:
            break
    else:
        nums.append(num)
print(nums)
