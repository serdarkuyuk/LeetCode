heights = [1,1,4,2,1,3]

target = sorted(heights)

# print(len(heights)-list(map(lambda x, y:x - y, heights, target)).count(0))
count = 0
for i,j in zip(heights,target):
    if (i - j) != 0:
        count += 1
print(count)
