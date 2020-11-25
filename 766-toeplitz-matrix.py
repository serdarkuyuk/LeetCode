matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

rlength = len(matrix)
clength = len(matrix[0])

for i in range(rlength-1):
    for i, j in zip(matrix[i][:-1],matrix[i+1][1:])
        if i != j:
            return False

return True
