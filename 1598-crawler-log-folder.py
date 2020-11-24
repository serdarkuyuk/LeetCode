logs = ["d1/","d2/","../","d21/","./"]
logs = ["d1/","d2/","./","d3/","../","d31/"]
logs = ["d1/","../","../","../"]
stack = []
for move in logs:
    if move not in ["../", "./"]:
        stack.append(move)
    if move == "../" and stack:
        stack.pop()

print(len(stack))

stack = 0
for move in logs:
    if move not in ["../", "./"]:
        stack += 1
    if move == "../" and stack:
        stack -= 1

print(stack)
