points = [[1,1],[3,4],[-1,0],[1,1],[3,4],[-1,0]]

#solution 1
distance = 0
for num in range(len(points)-1):
    x1, y1 = points[num][0], points[num][1]
    x2, y2 = points[num+1][0], points[num+1][1]
    distance += max(abs(y2-y1),abs(x2-x1))
print(distance)


#solution 2
for tup1, tup2 in zip(points[:-1:], points[1:]):
    x1, y1 = tup1[0], tup1[1]
    x2, y2 = tup2[0], tup2[1]
    distance += max(abs(y2-y1),abs(x2-x1))
    print(tup1,tup2)
print(distance)
