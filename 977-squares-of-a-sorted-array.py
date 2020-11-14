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
    if rightNumber**2 > leftNumber**2:
        ans.append(rightNumber**2)
        newA.pop()
    else:
        ans.append(leftNumber**2)
        newA.popleft()
print(ans[::-1])


#2 pointer solution
length = len(A)
j = 0
while j < length and A[j] < 0:
    j += 1
i = j - 1

ans = []
while j < length and 0 <= i:
    if A[i]**2 >= A[j]**2:
        ans.append(A[j]**2)
        j += 1
    else:
        ans.append(A[i]**2)
        i -= 1
while j < length:
    ans.append(A[j]**2)
    j+=1
while i >= 0:
    ans.append(A[i]**2)
    i-=1

print(ans)
