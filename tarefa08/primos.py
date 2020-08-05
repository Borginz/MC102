def filtra(primos,lista):
    '''
    Criar uma lista filtrada vazia, e analisar cada elemento da lista inicial e verificar se
    podera ser adicionado, pela condição primos, na lista_filtrada e devolver esta
    '''
    lista_filtrada = []
    for elemento in lista:
        if primos:
            lista_filtrada.append(elemento)
    return lista_filtrada
def mapeia(elevar_quadrado,lista):
    '''
    Criar uma lista_mapeada e aplicar em cada elemento a função elevar_quadrado e devolver
    a nova lista mapeada
    '''
    lista_mapeada = []
    for elemento in lista:
        lista_mapeada.append(elevar_quadrado(elemento))
    return lista_mapeada
def reduz(somar,lista):
    pass
def somar(lista):
    pass
def primos(lista):
    pass
def elevar_qaudrado(elemento):
    return elemento**2


def main():
    lista_entrada = [int(x) for x in input().split()]
    lista_filtrada = filtra(primos,lista_entrada)
    lista_mapeada = mapeia(elevar_quadrado,lista_filtrada)
    print(reduz(somar,lista_mapeada))


main()