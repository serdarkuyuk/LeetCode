words = ["gin", "zen", "gig", "msg"]
alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
myDict = dict(zip(alphabet, morse))
print(myDict)
newdict = {}
for word in words:
    totals = ''
    for s in word:
        totals += myDict[s]
    newdict[totals] = 1
print(len(newdict))
