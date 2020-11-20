salary = [4000,3000,1000,2000]
salary = [8000,9000,2000,3000,6000,1000]
maxim = float("-inf")
minim = float("inf")
sumation = 0
for num in salary:
    sumation += num
    if num < minim:
        minim = num
    if num > maxim:
        maxim = num

print((sumation - minim - maxim)/(len(salary)-2))
