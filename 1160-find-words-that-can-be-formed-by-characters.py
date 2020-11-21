words = ["cat","bt","hat","tree"]
words = ["hello","world","leetcode"]
chars = "atach"
chars = "welldonehoneyr"
from collections import Counter
seconddict = Counter(chars)
summa = 0
for word in words:
    mylist = (seconddict & Counter(word)).values()
    number = sum(mylist)
    if number == len(word):
        summa += number


# print(firsdict & seconddict)
print(summa)
