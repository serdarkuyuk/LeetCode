import collections
freq = collections.Counter()
def function(nums):
    i = 1
    cnt = 0
    for num in nums:
        print(freq)
        print(i, cnt, num)
        freq[num] += 1
        if num >= i:
            cnt += 1
        if cnt == i:
            cnt -= freq[i]
            i += 1
    return -1 if cnt + freq[i-1] != i - 1 else i - 1
arr = [0,4,3,0,4]
result = function(arr)
print(result)
