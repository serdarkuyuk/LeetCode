num =123
step = 0
while num:
    step += 1
    num = num/2 if num%2 == 0 else num-1
print(num, step)
