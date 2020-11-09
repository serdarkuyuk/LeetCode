class Solution:
    def romanToInt(self, s):
      h={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

      k=0
      if len(s) > 1:
        for i in range(1,len(s)):

          x1 = int(h[s[i-1]])
          x2 = int(h[s[i]])

          if x1 >= x2:
            t = x1
          else:
            t = -x1
          k += t
        k = k+ int(h[s[i]])  
      else:
        k = int(h[s[0]]) 
      
      print(k)
      return k
        
        
m=Solution().romanToInt("I")

m=Solution().romanToInt("MCMXCIV")
