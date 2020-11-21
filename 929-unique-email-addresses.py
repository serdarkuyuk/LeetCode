emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

myset = set()
for email in emails:
    i = 0
    ch = email[i]
    firstString = ''
    while True:
        if ch == "+" or ch == "@":
            break
        if ch != ".":
            firstString += ch
        ch = email[i+1]
        i += 1
    i = -2
    ch = email[-1]
    secondString = ''
    while True:
        if ch == "@":
            break
        secondString = ch + secondString
        ch = email[i]
        i -= 1
    myset.add(firstString+'@'+secondString)
print(myset, len(myset))
