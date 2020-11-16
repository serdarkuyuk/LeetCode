arr = [3,5,1]

arr.sort()
print(arr)
diff = arr[0] - arr[1]

for first, second in zip(arr[:-1],arr[1:]):
    print(first, second, diff)
    if first-second != diff:
        print(False)
        break
