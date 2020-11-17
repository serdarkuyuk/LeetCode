A= [4,2,5,7]
# even, odd, res = [], [], []
# for i in A:
#     odd.append(i) if i&1 else even.append(i)
#     if even and odd:
#         res.append(even.pop())
#         res.append(odd.pop())
#
# print(res)
#
# t = 0
# even, odd = [], []
# for i in range(len(A)):
#     odd.append(A[i]) if A[i]&1 else even.append(A[i])
#     if even and odd:
#         A[t] = even.pop()
#         A[t+1] = odd.pop()
#         t += 2
#
# print(A)
#
#
# odd = (i for i in A if i&1)
# even = (i for i in A if i&1 == 0)
# res = []
# for _ in range(len(A)//2):
#     res.append(next(even))
#     res.append(next(odd))
# return res


oddindex = 1
for evenindex in range(0, len(A), 2):
    if A[evenindex]&1:
        while A[oddindex]%2:
            oddindex += 2
        A[evenindex], A[oddindex] = A[oddindex],  A[evenindex]













j = 1
for i in range(0, len(A), 2):

    if A[i] % 2:
        # print(i,j)
        while A[j] % 2:
            j += 2
        # print(i,j, A)
        print(A[i], A[j])
        A[i], A[j] = A[j], A[i]
        print(A[i], A[j])
        # print(i,j,A)
print(A)
