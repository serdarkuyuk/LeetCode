s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
output = ""
myDict = dict(zip(indices, s))
for i in range(len(indices)):
    output += myDict[i]
print(output)
