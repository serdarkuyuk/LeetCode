num = 9669
mylist = []
while num:
    remainder = num%10
    mylist.append(remainder)
    num = (num - num%10)/10

for i in range(len(mylist)-1,-1,-1):
    if mylist[i] == 6:
        mylist[i] = 9
        break

newnumber = 0
for i,number in enumerate(mylist):
    newnumber += number * 10**i
print(int(newnumber))

num = 9669
print(str(num).replace('6','9',1))

nums = num
i = 1
while nums:
    remainder = nums%10
    if remainder == 6:
        remember = i
    nums //= 10
    i += 1
print(num+3*10**2)
