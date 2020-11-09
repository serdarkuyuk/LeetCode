str = "HeFASFsllo"

#solution 1
print(str.lower())

#soution 2 with dictionary
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

dict=dict(zip(upper, lower))

result = ""
for i in str:
    if i in upper:
        result += dict[i]
    else:
        result += i

print(result)

#solution 3 
result = ""
for i in str:
    if i >= "A" and i <= "Z":
        result += chr(ord(i) + 32)
    else:
        result += i
print(result)
