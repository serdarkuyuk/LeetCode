paths = [["B","C"],
        ["D","B"],
        ["C","A"]]
start = {i[0] for i in paths}
desti = {i[1] for i in paths}
print((desti-start).pop())


mydict = {}
for srt, dest in paths:
    mydict[srt] = dest

for _,dest in paths:
    if dest not in mydict:
        print(dest)
src, dest = zip(*paths)

print(dict(zip(zip(*paths))))
