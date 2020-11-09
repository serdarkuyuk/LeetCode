s = "RLRRLLRLRL"
# s = "RLRRRLLRLL"

count = output = 0
for c in s:
    count += 1 if c == "R" else - 1
    output += 1 if count == 0 else 0

print(output)
