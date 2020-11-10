prices = [8,4,6,2,3]
# prices = [1,2,3,4,5]
# prices = [10,1,1,6]

#solution
for i, num1 in enumerate(prices[:-1]):
    j = i + 1
    while j < len(prices):
        num2 = prices[j]
        if num2 <= num1:
            prices[i] -= num2
            break
        j += 1


# print(prices)
#solution with stack
A = [8,4,6,2,3]
print(A)
stack = []
for i, a in enumerate(A):
    while stack and A[stack[-1]] >= a:
        A[stack.pop()] -= a
    stack.append(i)
    print(i, a, stack)
print(A)
