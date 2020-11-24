A = "this apple is sweet sweet"
B = "this apple is sour"
A = "s z z z s"
B ="s z ejt"

def uniqueDict(sentence, myDictionary):
    for word in sentence.split():
        myDictionary[word] = myDictionary.get(word, 0) + 1
    
    return [word for word, count in myDictionary.items() if count ==1]
print(uniqueDict(A+" "+B, {}))
# uniqueDict(B,dB)
# print(list(set(dB.keys())^set(dA.keys())))
# print(dA, dB)
# print(set(A.split())^set(B.split()))
