lista_frequencia = [(4, "a"), (4, "b"), (5, "e"), (5, "c"), (5, "d"),(4,"c")]
lista_frequencia.sort(key = lambda x:x[0], reverse = True)
lista_frequencia.append((0,"palavra0"))
contador = 0
for k in range(len(lista_frequencia)-1):
    if lista_frequencia[k][1]!= lista_frequencia[k+1][1]:
        lista_frequencia[contador:k+1] = sorted(lista_frequencia[contador:k+1])
        contador = k+1
lista_frequencia.remove((0,"palavra0"))
print(lista_frequencia)