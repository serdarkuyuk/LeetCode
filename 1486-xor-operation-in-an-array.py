n = 10
start = 5
mylist = [start+2*i for i in range(n)]
result = reduce(lambda x, y:x ^ y, mylist)
print(mylist, result)


res = 0
for i in range(n):
    res ^= start + 2 * i
return res


# 010
# 100
# 110

print(2^4)
