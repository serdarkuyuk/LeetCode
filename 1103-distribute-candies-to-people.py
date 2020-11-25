candies = 7
num_people = 4
i = 1
mylist = [0] * num_people
while candies <= 7:
    mylist[i-1] = i
    candies -= i
    i += 1
    print(mylist, candies)
if candies > 0:
    mylist[-1] = candies

print(mylist)


[1 2 3 4]   10+0*4
6 7 8 9     10+5*4
16 17 18 19 10+10*4
36 37 38 39 10+31*4
