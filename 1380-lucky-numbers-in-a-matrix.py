matrix =   [[3,7,8],
            [9,11,13],
            [15,16,17]]


matrix = [  [1,10,4,2],
            [9,3,8,7],
            [15,16,17,12]]

mins = set(min(row) for row in matrix)
maxs = set(max(col) for col in zip(*matrix))

print(type((mins & maxs).pop()))
