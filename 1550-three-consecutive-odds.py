arr = [1,2,34,3,4,5,7,23,12]
count = 0
for num in arr:
    if num^1: count = 0
    else: count += 1
    if count == 3:
        return true
        break
else:
    return False
