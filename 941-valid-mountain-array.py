# arr = [0,3,2,1]
arr = [2,1]
#
i=0
while i < len(arr)-1:
    if arr[i+1] < arr[i]:
        break
    i += 1

j = len(arr)-1
while j >= 0:
    if arr[j] > arr[j-1]:
        break

    j -= 1
print(i,j)


# i, j = 0, len(arr)-1
# while i < j:
#     if arr[i] > arr[i+1] and arr[j] > arr[j-1]:
#         print(False)
#     i += 1
#     j -= 1
# print(True)
