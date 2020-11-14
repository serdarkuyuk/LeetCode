# nums1 = [1,2,3,0,0,0]
nums1 = [-1,-1,0,0,0,0]
nums2 = [-1,-1,0]
m = 2
n = 2

i=m-1
j=n-1
k=m+n-1
while i>=0 and j>=0:
    if nums1[i]>nums2[j]:
        nums1[k]=nums1[i]
        i-=1
    else:
        nums1[k]=nums2[j]
        j-=1
    k-=1
if j>=0:
    nums1[:k+1]=nums2[:j+1]

print(nums1)
# ind1 = len(nums1)-1
# while nums1[ind1] == 0:
#     ind1 -= 1
#     if ind1 < 0:
#         nums1 = nums2
#         break
#
# ind2 = len(nums2) - 1
# indf = len(nums1) - 1
# while ind1 >= 0 and ind2 >= 0:
#     # print(ind1, ind2)
#     # print(nums1, nums2)
#     if nums1[ind1] < nums2[ind2]:
#         nums1[indf] = nums2[ind2]
#         ind2 -= 1
#
#     else:
#         nums1[indf], nums1[ind1] =  nums1[ind1], nums1[indf]
#         ind1 -= 1
#     indf -= 1
# while ind2 >= 0:
#     nums1[indf] = nums2[ind2]
#     ind2 -= 1
#     indf -= 1
# print(nums1)
