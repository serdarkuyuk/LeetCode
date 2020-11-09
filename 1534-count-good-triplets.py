arr = [7,3,7,3,12,1,12,2,3]
a = 5
b = 8
c = 1

count = 0
length = len(arr)
for i in range(length-2):
    for j in range(i+1, length-1):
        if abs(arr[i]-arr[j]) <=a:
            for k in range(j+1,length):
                if abs(arr[j]-arr[k]) <=b and abs(arr[i]-arr[k]) <= c:
                    count += 1

print(count)
