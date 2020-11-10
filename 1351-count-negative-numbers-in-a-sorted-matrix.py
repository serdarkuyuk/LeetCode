grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]

# grid = [[3,2],[1,0]]
# grid = [[1,-1],[-1,-1]]
# grid = [[-1]]
#O(mn) solution
count = 0
for row in grid:
    for number in row[::-1]:
        if number >= 0: break
        count += 1

print(count)

#O(m+n) solution
row = len(grid)-1
col = 0
count = 0
while row>=0 and col < len(grid[0]):
    # print(row,col)
    if grid[row][col] < 0:
        count +=len(grid[0])-col
        row -= 1
    else:
        col +=1
print(count)

#O(mlogn) binary search
def binarySearch(row):
    end = len(row)
    start = 0

    while start < end:
        mid = (start + end) // 2
        if row[mid] < 0:
            end = mid
        else:
            start = mid + 1
    return len(row)-start

count = 0
for row in grid:
    count += binarySearch(row)

print(count)
