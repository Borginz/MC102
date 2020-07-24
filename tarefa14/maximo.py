def achar_maximo(lista):
    if len(lista) == 1:
        maximo = lista[0]
        return maximo
    else:
        maximo = achar_maximo(lista[1:])
        if lista[0] > maximo:
            maximo = lista[0]
        return maximo





def main():
    lista = [int(x) for x in input().split()]
    print(achar_maximo(lista))
main()