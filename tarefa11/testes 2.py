dict = {"coelho" : 4,"sapo" : 3,"lontra" : 2,"cabra" : 1, "bode" : 1}
tuplas = []
for k,v in dict.items():
    tuplas.append((k,v))
tuplas.sort(key=lambda x: x[1], reverse = True)
tuplas.append((0, "palavra0"))
contador = 0
for k in range(len(tuplas) - 1):
    if tuplas[k][0] != tuplas[k + 1][0]:
        tuplas[contador:k + 1] = sorted(tuplas[contador:k + 1])
        contador = k + 1
tuplas.remove((0, "palavra0"))
print(tuplas)




