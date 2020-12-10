S = "leetcodeisacommunityforcoders"

s = ''
for i in S:
    if i not in set("eaiou"):
        s += i
print(s)




return re.sub("[aeiou]+","",S)
