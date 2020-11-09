# candies = [2,3,5,1,3]
# extraCandies = 3
candies = [4,2,1,1,2]
extraCandies = 1
mylist = []
candies2max = max(candies) - extraCandies

#soution 1 with append
for candie in candies:
    mylist.append(candie >= candies2max )

#solution 2 with list comprehension
mylist = [candie >= candies2max for candie in candies]

print(mylist)
