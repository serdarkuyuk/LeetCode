moves = "UD"# "LDRRLRUULR"
x, y = 0, 0
for move in moves:

    if move == "L": x -= 1
    if move == "R": x += 1
    if move == "U": y += 1
    if move == "D": y -= 1
    print(x,y)

if x == 0 and y == 0:
    print(True)
print(False)
