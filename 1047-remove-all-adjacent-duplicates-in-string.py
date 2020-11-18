S = list("abbaca")
mylist = []

for s in S:
    if mylist and s == mylist[-1]:
        mylist.pop()
    else:
        mylist.append(s)


print("".join(mylist))


	x, y = 1, z
	pairs = []

	while x<=z and y>0:
		cf = customfunction.f(x,y)
		if cf==z:
			pairs.append([x,y])
			x, y = x+1, y-1
		elif cf > z:
			y -= 1
		else:
			x += 1
	return pairs
