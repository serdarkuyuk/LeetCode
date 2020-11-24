candies = 7
num_people = 4
i = 1
mylist = [0] * num_people
while candies <= 0:
    mylist[i-1] = i
    candies -= i
    i += 1
    print(mylist, candies)
if candies > 0:
    mylist[-1] = candies

print(mylist)
