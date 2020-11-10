# coding=utf-8
s = "123456789"
s2= "10#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output = "abcdefghijklmnopqrstuvwxyz"
# for i in s[::-1]:
#     if i == "#"
# ç
#     print(i)
mylist1 = list(s)
mylist2 = [s2[i:i+3] for i in range(0,len(s2),3)]
mylist = mylist1 + mylist2
charters = list(Output)
mydict = dict(zip(mylist, charters))

print(mydict)


# s = "10#11#12"
# s = "1326
s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
mystr = ""
i = 0
while i < len(s):
    if i+2 < len(s) and s[i+2] == "#":
        mystr += mydict[s[i:i+3]]
        i += 3
    else:
        mystr += mydict[s[i]]
        i += 1
print(mystr)
