grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
print(grid[0][0])

# grid = [[1]]
# grid = [[1,0]]
# edgedic = {4:0, 3:1, 2:2, 1:3, 0:0}
# moves = [[1,0],[-1,0],[0,1],[0,-1]]
# total = 0
# for r in range(len(grid)):
#     for c in range(len(grid[0])):
#         count = 0
#         if grid[r][c] == 1:
#             for move in moves:
#                 newr = r+move[0]
#                 newc = c+move[1]
#                 # print(newr,newc)
#                 if newr >= 0 and newr<len(grid) and newc >= 0 and newc < len(grid[0]) and grid[newr][newc] == 1:
#                     count += 1
#                     # print(count, r, c)
#         total += edgedic[count]
# total = total if total !=0 else 4
# print(total)
from collections import deque
# grid = [[1,0]]
def counter(location, moves, total):
    r, c = location
    count = 0
    for move in moves:
        newr, newc = r + move[0], c + move[1]
        if newr >= 0 and newr<len(grid) and newc >= 0 and newc < len(grid[0]) and grid[newr][newc] == 1:
            count += 1
    total += edgedic[count]
    return count, edgedic[count], total

visited = set()
edgedic = {4:0, 3:1, 2:2, 1:3, 0:0}
moves = [[1,0],[-1,0],[0,1],[0,-1]]
total = 0
mylocation = []
queue = deque()
flag = True
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 1:
            queue.append([r, c])
            # print(total)
            print(counter([r, c],moves, total))
            # mylocation.append([r,c])
            while queue:
                r, c = queue.popleft()

                # grid[r][c] = 0
                visited.add((r,c))
                for move in moves:
                    newr, newc = r + move[0], c + move[1]
                    if newr >= 0 and newr<len(grid) and newc >= 0 and newc < len(grid[0]) and grid[newr][newc] == 1 and (newr, newc) not in visited:
                        queue.append([newr, newc])
                        # print(counter([newr, newc],moves))
                        # visited.add((newr, newc))
                        # print(queue)
 # flag = False
                # mylocation.append([newr,newc])
            # print(r,c, mylocation)
# print(mylocation)
