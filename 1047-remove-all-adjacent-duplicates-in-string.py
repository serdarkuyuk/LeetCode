S = list("abbaca")
mylist = []

for s in S:
    if mylist and s == mylist[-1]:
        mylist.pop()
    else:
        mylist.append(s)


print("".join(mylist))
