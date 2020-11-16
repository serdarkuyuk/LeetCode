# arr = [0,3,2,1]
arr = [2,1]
#
if len(arr) < 3:
    return False

i=0
while i < len(arr)-1:
    if arr[i+1] <= arr[i]:
        break
    i += 1

j = len(arr)-1
while j >= 0:
    if arr[j] >= arr[j-1]:
        break
    j -= 1

if i == j and i != 0 and j != len(arr)-1:
    return True
return False
