def achar_ausente(lista):
    if lista[1] != (lista[0]+1):
        ausente = lista[0]+1
        return ausente
    else:
        ausente = achar_ausente(lista[1:])
        return ausente









def main():
    lista = [int(x) for x in input().split()]
    print(achar_ausente(lista))
main()