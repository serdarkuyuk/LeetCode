position = [1,2, 2, 4, 3, 3,3]

# solution  1
from collections import Counter
mydict = Counter(position)
print(mydict)
even = odd = 0
for key in mydict:
    if key % 2 == 0:
        even += mydict[key]
    else:
        odd += mydict[key]
print(min(even, odd))

# soution 2
even = odd = 0
for num in position:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

for number in position:
    if number&1:
        odd += 1
    else:
        even += 1

evenodd = [0, 0]
for p in position:
    evenodd[p % 2] += 1
print(min(evenodd))
