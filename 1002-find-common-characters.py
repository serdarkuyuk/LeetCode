A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
# A = ["bella","label","roller"]
# A =["cool","lock","cook"]
import collections
m = collections.defaultdict(lambda:[0]*len(A))

# alphabetDict = defaultdict(list)
for i in range(len(A)):
    for char in A[i]:
        if char not in m:
            m[char][i] = 1
        else:
            m[char][i] += 1
res = []
for key,values in m.items():
    value = min(values)
    if value != 0:
        res.extend(key*value)
print(res)

# from collections import defaultdict
# alphabetDict = defaultdict(list)
# alphabetDict = {chr(i):[] for i in range(97,123,1)}
# for word in A:
#     visited = set()
#     for s in word:
#         if s not in visited:
#             alphabetDict[s] += [word.count(s)]
#             visited.add(s)
#
# mylist = []
# length = len(A)
# for alpha, lists in alphabetDict.items():
#     if alpha and len(lists) == length:
#         for i in range(min(lists)):
#             mylist.append(alpha)
#
# print(alphabetDict)
# print(mylist)
#

# res = []
# key_set = set(A[0])
# for ch in key_set:
#     print([w.count(ch) for w in A])
#     n = min([w.count(ch) for w in A])
#     if n:
#         res.extend([ch]*n)
#
# print(res)
