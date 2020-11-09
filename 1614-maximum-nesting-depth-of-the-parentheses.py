s = "(1+(2*3)+((8)/4))+1"
# s = "(1)+((2))+(((3)))"
# s = "1+(2*3)/(2-1)"
s = "8*((1*(5+6))*(8/6))"
#solution 1 with stack
depth = 0
stack = []
for i in s:
    if i == "(":
        stack.append(i)
        depth = max(len(stack), depth)
    elif i == ")":
        stack.pop()
print(depth)

#solution 2
depth = 0
count = 0
for i in s:
    if i == "(":
        count += 1
        depth = max(count, depth)
    elif i == ")":
        count -= 1
print(depth)
