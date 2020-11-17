target = [4]
# n = 3
# mylist = []
# for num in range(1,max(target)+1):
#     mylist.append("Push")
#     if num not in target:
#         mylist.append("Pop")
# print(mylist)

mylist = []
currentNumber = 1
for num in target:

    while currentNumber < num:
        mylist.extend(["Push", "Pop"])
        currentNumber += 1

    mylist.append("Push")
    currentNumber = num+1
print(mylist)
