s = "aaaabbbbcccc"
# s = "leetcode"
# s = "rat"
# s = "ggggggg"

#solution
slist = list(s)
result = ''
while slist:
    charset = set(slist)
    while charset:
        minchr = min(charset)
        result += minchr
        slist.remove(minchr)
        charset.remove(minchr)
    charset = set(slist)
    while charset:
        maxchr = max(charset)
        result += maxchr
        slist.remove(maxchr)
        charset.remove(maxchr)
print(result)

#solution with sort
import collections
d = sorted([c, n] for c, n in collections.Counter(s).items())
r = []
while len(r) < len(s):
    for i in range(len(d)):
        if d[i][1]:
            r.append(d[i][0])
            d[i][1] -= 1
    for i in range(len(d)):
        if d[~i][1]:
            r.append(d[~i][0])
            d[~i][1] -= 1
return ''.join(r)
