edge = len(arr) // 20
arr.sort()
return sum(arr[edge:-edge])/(len(arr)-2*edge)
