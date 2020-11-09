# mat = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]

mat = [ [7,3,1,9],
        [3,4,6,9],
        [6,9,6,6],
        [9,5,8,5]]

summation = 0

for i in range(len(mat[0])):
    summation += (mat[i][i] + mat[i][-i-1])
if len(mat[0]) % 2 == 1:
    mid = len(mat[0])//2
    summation -= mat[mid][mid]
print(summation)
