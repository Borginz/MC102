def transformar_int(lista):
    lista_int = []
    for i in lista:
        i=int(i)
        lista_int.append(i)
    return lista_int
def soma(lista):
  soma = 0
  for numero in lista:
    soma += numero
  return soma


def primos(i):
    n=0
    if i>1:
        for k in range(2, int(i**0.5) +1):
            if i % k == 0:
                 n=+1
    else:
        n+=1
    if n == 0:
        return True
    else:
        return False

def filtra(lista_int, primos):
    lista_filtrada = []
    for i in lista_int:
        if primos(i):
            lista_filtrada.append(i)
    return lista_filtrada

def mapeia(lista_filtrada, quadrados):
    lista_mapeada = []
    for i in lista_filtrada:
        lista_mapeada.append(quadrados(i))
    return lista_mapeada

def quadrados(lista_mapeada):
    for i in lista_mapeada:
        lista_mapeada[i]=lista_mapeada[i]**2
    return lista_mapeada

def reduz(lista_mapeada, soma):
    if len(lista_mapeada) > 0:
        reduzida = lista_mapeada[0]
        for i in range(1, len(lista_mapeada)):
            reduzida = soma(lista_mapeada)
    else:
        reduzida = 0
    return reduzida
def quadrados(i):
    return i**2

def main():
    lista = input().split()
    lista_int = transformar_int(lista)
    lista_filtrada = filtra(lista_int, primos)
    lista_mapeada = mapeia(lista_filtrada, quadrados)
    print(reduz(lista_mapeada, soma))

main()
