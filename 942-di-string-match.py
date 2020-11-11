S = "DDIDDDIIDIDIDIIDDIIIID"
smallest = 0
largest = len(S)
mylist = []
for i in S:
    if i == "I" :
        mylist.append(smallest)
        smallest += 1
    if i == "D" :
        mylist.append(largest)
        largest -= 1
print(mylist+[smallest])
