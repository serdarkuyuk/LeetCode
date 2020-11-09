n = 1

mylist = []
summation = 0
multiplication = 1
if not n:
    return 0
while n:
    digit = n % 10
    n = n // 10
    summation += digit
    multiplication *= digit
    # mylist.append(digit)
print(multiplication-summation)
