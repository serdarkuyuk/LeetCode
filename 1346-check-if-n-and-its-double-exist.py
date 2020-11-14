# arr = [10,2,5,3]
arr = [-2,0, 0,10,-19,4,6,-8]
# arr = [0,0]
mydict = {}

for num in arr:
    if num in mydict:
        mydict[num] += 1
    else:
        mydict.setdefault(num, 1)
# i = 0
for num in arr:
    # print(arr[i],arr[mydict[num]])
    if num and num*2 in mydict or mydict[0] >= 2:
        print(True)
        break
    # i += 1
print(str(mydict))
