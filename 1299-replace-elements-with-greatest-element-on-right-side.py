arr = [17,18,5,4,6,1]
maxNumber = -1
for i in range(1,len(arr)):
    maxNumber = max(maxNumber, arr[~i])
    arr[~i] = maxNumber
# arr.pop(0)
arr.append(-1)
print(arr)

#second solution
arr = [17,18,5,4,6,1]
me = arr[-1]
arr[-1] = -1
for i in range(len(arr)-2,-1,-1):
    me, arr[i] = max(me,arr[i]), me
print(arr)
