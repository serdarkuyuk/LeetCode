S = "abaa"
C = 'b'

mylist = []
count = float("Inf")
for ch in S:
    if ch == C : count = 0
    else: count += 1
    mylist.append(count)
print(mylist)
count = float("Inf")
for i, num in enumerate(range(len(S))):
    if mylist[~i] == 0: count = 0
    else:
        count += 1
        mylist[~i] = min(count, mylist[~i])

print(mylist)
