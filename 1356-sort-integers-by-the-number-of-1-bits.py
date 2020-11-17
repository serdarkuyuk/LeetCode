arr = [0,1,2,3,4,5,6,7,8]
# arr = [1024,512,256,128,64,32,16,8,4,2,1]

def countbit(num):
    count = 0
    while num:
        num &= (num-1)
        count += 1
    return count

mylist = [(countbit(num), num) for num in arr]
# mydict = {}
# for num in arr:
#     mydict[num]= countbit(num)

# print([x for _, x in sorted(zip(mydict.values(), mydict.keys()))])
print([x for _, x in sorted(mylist)])
