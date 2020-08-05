def filtra(primos,lista):
    pass
def mapeia(elevar_quadrado,lista):
    pass
def reduz(somar,lista):
    pass
def somar(lista):
    pass
def primos(lista):
    pass
def elevar_qaudrado(lista):


def main():
    lista_entrada = [int(x) for x in input().split()]
    lista_filtrada = filtra(primos,lista_entrada)
    lista_mapeada = mapeia(elevar_quadrado,lista_filtrada)
    print(reduz(somar,lista_mapeada))


main()