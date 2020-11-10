from collections import deque
given = [3,1,2,4]
mylist = deque()

for number in given:
    if number%2 == 0:
        mylist.appendleft(number)
    else:
        mylist.append(number)
print(mylist)
