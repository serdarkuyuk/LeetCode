dicti = {0: 1, 1: 1, 2: 2, 3: 1, 4: 1, 5: 6, 6: 1, 7: 1, 8: 1, 9: 1}

for i in range(10):
    dicti[i]=dicti.get(i,0)+1

print(dicti)
