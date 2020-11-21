# not solved
nums = [1,1,2,2,2,3]
mydic = {}
for num in nums:
    mydic[num] = mydic.get(num, 0) + 1
print(sorted(mydic.items()))
