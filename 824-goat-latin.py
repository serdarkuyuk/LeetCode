vowels = 'aeiouAEIOU'
print(set(vowels))
# mylist = S.split(" ")
# for i, word in enumerate(mylist):
#     if word[0] in vowels:
#         mylist[i] = word + "ma" + 'a'*(i+1)
#     else:
#         mylist[i] = word[1:] + word[0] + 'ma' + 'a'*(i+1)
# return " ".join(mylist)
#
#
# class Solution:
#     def toGoatLatin(self, S: str) -> str:
#         def proc(idx, word):
#             if word[0] not in 'aeiouAEIOU':
#                 word = word[1:] + word[0]
#
#             return word + 'ma' + ('a' * idx)
#
#         return ' '.join([proc(i, w) for i, w in enumerate(S.split(), 1)])
