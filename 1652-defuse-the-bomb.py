code = [5,7,1,4]
k = -3
ranger= [1, abs(k+1)] if k>0 else [k, 0]

# i 0   0:0+3
mylist = []
for c in range(len(code)):
    sum = 0
    for index in range(ranger[0], ranger[1]):
        sum += code[(c+index)%len(code)]
    mylist.append(sum)
print(mylist)
