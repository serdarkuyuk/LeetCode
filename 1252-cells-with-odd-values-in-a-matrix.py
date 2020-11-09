n = 2
m = 3
indices = [[0,1],[1,1]]
# n = 2
# m = 2
# indices = [[1,1],[0,0]]

matrix = [[0]*m]*n
rows = [i[0] for i in indices]
colums = [i[1] for i in indices]

for row in rows:
    matrix[row] = map(lambda x:x+1, matrix[row])

for column in colums:
    for k in range(len(matrix)):
        matrix[k][column] += 1

print(matrix)
