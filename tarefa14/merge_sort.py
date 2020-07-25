def ordenar(lista):
    if lista[0] < lista[1]:
        aux = lista[0]
        lista[0] = lista[1]
        lista[1] = aux
        return lista
    else:
        



def main():
    lista = [int(x) for x in input().split()]
    ordenar(lista)