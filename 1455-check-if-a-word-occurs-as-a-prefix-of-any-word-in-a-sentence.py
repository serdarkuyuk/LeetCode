# sentence = "i love eating burger"
# searchWord = "burg"
sentence = "i am tired"
searchWord = "you"
i, count = 0, 1
while i < len(sentence):
    if sentence[i] != searchWord[0]:
        while i<len(sentence) and sentence[i] != " ":
            i += 1
        count += 1
    if i<len(sentence) and sentence[i] == searchWord[0]:
        if sentence[i+1:i+1+len(searchWord)-1] == searchWord[1:]:
            print(count)
            break
    # else:
    #     print(-1)
    i += 1
else:
    print(-1)
