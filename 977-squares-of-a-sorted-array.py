A = [-4,-1,0,1,2,6,10]

# qeue solution
from collections import deque
newA = deque(A)
left = 0
right = len(A)
ans =[]
while newA:
    leftNumber = newA[0]
    rightNumber = newA[-1]
    print(leftNumber, rightNumber)
    if rightNumber**2 > leftNumber**2:
        ans.append(rightNumber**2)
        newA.pop()
    else:
        ans.append(leftNumber**2)
        newA.popleft()
# ans.append(newA.pop())
print(ans[::-1])



# 2 pointer solution
# length = len(A)
# j = 0
# while j < length and A[j] < 0:
#     j += 1
# i = j - 1
#
# ans = []
# while j < length and 0 <= i:
#     if A[i]**2 >= A[j]**2:
#         ans.append(A[j]**2)
#         j += 1
#     else:
#         ans.append(A[i]**2)
#         i -= 1
# while j < length:
#     ans.append(A[j]**2)
#     j+=1
# while i >= 0:
#     ans.append(A[i]**2)
#     i-=1
#
# print(ans)
#
#
#
#
#
#
#
#
#
#
#
#
#


# inputSquares = list(map(lambda x : x*x, input))
# print(sorted(inputSquares))
# import collections
# number_deque = collections.deque(A)
# reverse_sorted_squares = []
# while number_deque:
#     print(number_deque, reverse_sorted_squares)
#     left_square = number_deque[0] ** 2
#     right_square = number_deque[-1] ** 2
#     if left_square > right_square:
#         reverse_sorted_squares.append(left_square)
#         number_deque.popleft()
#     else:
#         reverse_sorted_squares.append(right_square)
#         number_deque.pop()
# print(reverse_sorted_squares[::-1])
