import copy
A = [[1,1,0],[1,0,1],[0,0,0]]
B = copy.deepcopy(A)
for row in range(len(A)):
    k = 0
    for i in range(len(A[0])-1,-1,-1):
        B[row][k] = 1 - A[row][i]
        k += 1
print(B)


for row in A:
    for i in range((len(row)+1)/2):
        row[i], row[-i] = row[-i]^1, row[i]^1
print(A)
