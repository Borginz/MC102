def filtra(primos,lista):
    '''
    Criar uma lista filtrada vazia, e analisar cada elemento da lista inicial e verificar se
    podera ser adicionado, pela condição primos, na lista_filtrada
    '''
    lista_filtrada = []
    for elemento in lista:
        if primos:
            lista_filtrada.append(elemento)
    return lista_filtrada
def mapeia(elevar_quadrado,lista):
    pass
def reduz(somar,lista):
    pass
def somar(lista):
    pass
def primos(lista):
    pass
def elevar_qaudrado(lista):
    pass


def main():
    lista_entrada = [int(x) for x in input().split()]
    lista_filtrada = filtra(primos,lista_entrada)
    lista_mapeada = mapeia(elevar_quadrado,lista_filtrada)
    print(reduz(somar,lista_mapeada))


main()