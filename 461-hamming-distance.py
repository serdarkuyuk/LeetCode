x = 1
y = 4
ny = bin(4)
nx = bin(1)
# print(type(ny[2:]))
# print(nx[2:])
# print(bin(x^y)[2:])
# print(bin(4)[2:])
count = 0
number = x ^ y

while number != 0:
    # print(number)
    # number = number & number-1
    number >>= number
    count += 1

print(count)

y=4
print(y << 1)
# string
