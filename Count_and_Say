The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.


class Solution:
    def countAndSay(self, n):
        nn=[1]
        lists=[]
        for ik in range(n-1):
            count = 1
            nn.append(0)
            for i in range(len(nn)-1):              
                if nn[i] == nn[i+1]:
                    count = count +1
                else:                
                    lists.append(count)
                    lists.append(nn[i])
                    count=1             
            n=[]
            nn = lists
            lists=[]
 
        return "".join([str(elem) for elem in nn])
