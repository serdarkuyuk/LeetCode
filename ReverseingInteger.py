class Solution:
    def reverse(self, x):
        s = str(abs(x))
            
        ters = int(s[::-1])
        
        if ters > 2**31-1:
            return 0

        return ters if x > 0 else (ters * -1)
