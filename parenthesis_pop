class Solution:
    def isValid(self, s):
        table={")":"(","}":"{","]":"["}
        memory=[]
        for i in s:
            if i in table:
                top=memory.pop() if memory else '#'
                if table[i] != top:
                    return False
            else:
                memory.append(i)
        if len(memory) == 0: 
            return True
        else: 
            return False
