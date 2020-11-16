str = "I speak Goat Latin"
str = "Wala The quick brown fox jumped over the lazy dog"
vowels = 'aeiouAEIOU'
mylist = str.split(" ")
print(mylist)
for i, word in enumerate(mylist):
    if word[0] in vowels:
        mylist[i] = word + "ma" + 'a'*(i+1)
    else:
        mylist[i] = word[1:] + word[0] + 'ma' + 'a'*(i+1)
print(" ".join(mylist))
