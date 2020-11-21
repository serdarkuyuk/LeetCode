arr = [4,2,1,3]
arr = [3,8,-10,23,19,-4,-14,27]
arr.sort()
minimum = float("Inf")
for i, j in zip(arr[:-1],arr[1:]):
    minimum = min(minimum, abs(i - j))
# for i, j in zip(arr[:-1],arr[1:]):
#     :
mylist = [[i,j] for i, j in zip(arr[:-1],arr[1:]) if abs(i - j) == minimum]
print(mylist)


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum, mylist= float("Inf"), []
        for a, b in zip(arr[:-1],arr[1:]):
            difference = b-a
            if difference == minimum: mylist.append([a, b])
            if difference < minimum: mylist, minimum = [[a, b]], difference
        return mylist
