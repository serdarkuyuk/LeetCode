arr = [-3,0,1,-3,1,1,1,-3,10,0]

from collections import Counter

mydict= Counter(arr)
# myset = set()
# for key in mydict:
#     myset.add()

myset = {val for val in mydict.values()}
print(len(mydict) == len(myset))
