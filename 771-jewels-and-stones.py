J = "aA"
S = "aAAbbbb"

count = 0
for s in S:
    if s in J:
        count += 1

print(count)

print(sum(map(J.count, S)))
print(sum(map(S.count, J)))

# from collections import Counter
# print(Counter(S))

#solution 3 membership operation in set is O(1)
jSet = set(J)
count = 0
for s in S:
    if s in jSet:
        count += 1
print(count)
