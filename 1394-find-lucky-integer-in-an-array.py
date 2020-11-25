arr = [1,2,2,3,3,3]

mydict = {}
for num in arr:
    mydict[num] = mydict.get(num, 0) + 1

count = -1
for key, value in mydict.items():
    if key == value:
        count = max(count, key)

print(count)
