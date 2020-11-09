
str = "(()())(())(()(()))"

result = pop = ""
stack = []
for s in str:
    result += s
    stack.append("(") if s == "(" else stack.pop()
    if not stack:
        pop += result[1:-1]
        result = ""
print(pop)
