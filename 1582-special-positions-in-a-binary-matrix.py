mat = [[0,0,0,1],
       [1,0,0,0],
       [0,1,1,0],
       [0,0,0,0]]
# mat = [[1,0,0],
#         [0,0,1],
#         [1,0,0]]


row_sums = list(map(sum, mat))
col_sums = list(map(sum, zip(*mat)))
print(row_sums, col_sums)
count = 0
for r, row in enumerate(mat):
    for c, n in enumerate(mat[r]):
        print(r, c, n)
        if n and row_sums[r] == col_sums[c] == 1:
            count += 1

print(count)
# myRow = []
# for i, row in enumerate(mat):
#     if sum(row) == 1:
#         myRow.append(i)
# print(myRow)
#
# myColumn = []
# for i, column in enumerate(zip(*mat)):
#     if sum(column) == 1:
#         myColumn.append(i)
# print(myColumn)
#
# count = 0
# for r in myRow:
#     for c in myColumn:
#         if mat[r][c] == 1:
#             count += 1
# print(count)
