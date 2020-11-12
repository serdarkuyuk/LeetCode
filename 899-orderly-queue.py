S = list("cba")
# S = "baaca"
# length = len(S)
# i = 0
# while i < length-1:
#     print(S[i]>S[i+1])
#     if S[i]>S[i+1]:
#         i += 1
#         S.append(S[i])
#         S.remove(S[i])
#         print(S)
#         i -= 1
#     i += 1
# print(''.join(S))

K=2
if K > 1:
    ss = list(S)
    ss.sort()
    print("".join(ss))
ss = []
for i in range(len(S)):
    print(ss, S[i:], S[:i])
    ss.append(S[i:] + S[:i])
ss.sort()
print(ss[0])
