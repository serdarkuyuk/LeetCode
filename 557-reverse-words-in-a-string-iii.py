s ="Let's take LeetCode contest"
i, mystr, length = 0, '', len(s)
#counter
while i < length:
    word = ''
    while i<length and s[i] and not s[i].isspace():
        word = s[i] + word
        i += 1
    mystr = mystr + word + ' '
    i += 1

print(mystr[:-1])
print(mystr)
