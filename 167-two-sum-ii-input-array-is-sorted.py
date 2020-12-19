class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        htable = dict()
        lengthNums = len(numbers)
        i = 0
        while i < lengthNums:
            if numbers[i] in htable:
                return [htable[numbers[i]]+1, i+1]
            else:
                htable[target - numbers[i]] = i
            i += 1

        def twoSum2(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i
