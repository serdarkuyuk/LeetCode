from math
nums = [12,345,2,6,7896]


count = 0
for num in nums:
    if (int(log10(abs(num)))+1)%2 == 0:
        count += 1
print(count)
