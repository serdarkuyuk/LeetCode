words = ["mass","as","hero","superhero"]

words.sort(key=len)
mylist = []
i = 0
while i in range(len(words)):
    for word in words[i+1:]:
        # print(words)
        if len(words[i]) <= len(word):
            if words[i] in word:
                mylist.append(words[i])
    i += 1

print(mylist)
