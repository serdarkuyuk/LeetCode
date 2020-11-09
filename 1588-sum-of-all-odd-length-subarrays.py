arr = [1,4,2,5,3]
summation = 0

for level in range(1, len(arr)+2, 2):
    i = 0
    while i+level < len(arr)+1:
        summation += reduce(lambda x,y: x+y, arr[i:i+level])
        i += 1

print(summation)
