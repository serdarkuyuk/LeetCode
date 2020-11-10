nums = [3,7]

#solution
max = [0, 0]
for i in nums:
    if i > max[0]:
        max[1] = max[0]
        max[0] = i
    elif max[1] < i <= max[0]:
        max[1] = i
print((max[0]-1)*(max[1]-1))

#pythonic solution
first, second = 0, 0
for number in nums:
    if number > first:
        first,  second = number, first
    else:
        second = max(second, number)
print((first-1)*(second-1))

#even better solution
first, second = 0, 0
for number in nums:
    first, second = max(first, number), max(second, min(number, first))
print((first-1)*(second-1))
