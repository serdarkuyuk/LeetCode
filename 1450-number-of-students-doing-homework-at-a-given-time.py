startTime = [9,8,7,6,5,4,3,2,1]


endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5
count=0
for s, e in zip(startTime, endTime):
    if queryTime < s: continue
    if queryTime > e: continue
    if s <= queryTime and queryTime <= e:
        count += 1
print(count)
