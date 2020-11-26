import heapq

stones = [2,7,4,1,8,1]
print(stones)
stones = [-i for i in stones]

heapq.heapify(stones)  # make heap structure
while stones and len(stones) >= 2:
    difference = heapq.heappop(stones) - heapq.heappop(stones)
    print(difference, stones)
    heapq.heappush(stones, difference) if difference != 0 else None
print(stones if stones else 0)

# heapq.heappush(list, number)
#
# heapq.heappop(list) # pop the root element (smallest element)
#
# heapq.heappushpop(list, number)
