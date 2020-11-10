import random

n=13
#solution 1
if n % 2 == 0:
    myList = [i for i in range(1,n/2+1)] + [-i for i in range(1,n/2+1)]
else:
    myList = [i for i in range(1,n/2+1)] + [0] + [-i for i in range(1,n/2+1)]
print myList

#solution 2
print(list(range(1,n))+[-n*(n-1)//2])

#solution 3
print(list(range(-(n//2), 0)) + [0]*(n % 2) + list(range(1, n//2 + 1)))

n=14

#solution 4
if n == 1:
    return [0]
myList = []
numbers = {}
summation = 0
while len(myList) < n-1:
    number = random.randint(1, 100000)
    if number not in numbers:
        numbers[number] = 1
        myList.append(number)
        summation += number
myList.append(-summation)
print(myList)
