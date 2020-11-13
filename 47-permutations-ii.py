nums = [1,2,3]

# def dfs(decSpace, path, result):
#     if not decSpace:
#         result.append(path)
#         return
#
#     for i in range(len(decSpace)):
#         print(decSpace[:i]+decSpace[i+1:], path+[decSpace[i]], result)
#         dfs(decSpace[:i]+decSpace[i+1:], path+[decSpace[i]], result)
#
#
# result = []
# result = dfs(nums,[],result)
# print(result)
class Tree:
    def DFS(self,path,recoder):
      if len(path) == self.length:
          self.res.append(path)

      for key in recoder:
          if recoder[key] > 0:
              recoder[key] -= 1
              print(recoder, path+[key])
              self.DFS(path+[key],recoder)
              recoder[key] += 1


    def permute(self, nums):
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
      self.length = len(nums)
      import collections
      recoder = collections.Counter(nums)
      print(recoder)
      self.res = []
      self.DFS([],recoder)
      return self.res
print(Tree().permute(nums))
