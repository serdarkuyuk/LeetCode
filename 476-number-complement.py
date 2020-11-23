num = 5
import math
# number = bin(num)[2:]
# print(number)
# print(bin(~num)[2:])
# while num:
#     num = num >> 1
#     print(num)
# print(num ^ (2**num.bit_length() - 1))
# print(num^)
exponent = int(math.log(num,2))+1
allones = 2**exponent-1
print(allones^num)
# num = 5
# print(int(math.log(num,2))+1)
