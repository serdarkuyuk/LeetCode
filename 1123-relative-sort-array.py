from collections import Counter

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

# mydict = Counter(arr1)
# mylist = []
# for i in arr2:
#     mylist += [i] * mydict[i]
#     mydict.pop(i)
#
# restNumbers = []
# for key,val in mydict.items():
#     restNumbers += [key]*val
#
# mylist.extend(sorted(restNumbers))

mydict = {num:0 for num in arr2}

restNumbers = []
for num in arr1:
    if num in mydict:
        mydict[num] += 1
    else:
        restNumbers.append(num)

mylist = []
for key,val in mydict.items():
    mylist += [key]*val
mylist.extend(sorted(restNumbers))
print(mylist)
