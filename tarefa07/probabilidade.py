def maior_da_lista(lista):
    '''função para achar o maior numero da lista'''
    maior = 0
    for i in lista:
        i = int(i)
        if i > maior:
            maior = i
    return maior
def inteirar(lista):
    '''Função para transformar as 'str''em int'''
    for i in lista:
        i = int(i)
    return lista
def contar_frequencia(lista,maior):
    '''função para contar a frequencia e assim a probabilidade de cada numero'''
    frequencia = [0] * (maior + 1)
    for i in lista:
        i = int(i)
        frequencia[i]+= 1
    return frequencia
def tirar_zeros(lista):
    '''funçao para tirar os zeros da lista de frequencia deixando em ordem'''
    frequencia_sem_zeros = []
    for i in lista:
        if i != 0:
            frequencia_sem_zeros.append(i)
    return frequencia_sem_zeros
def tirar_repeticao(lista):
    ''' função para tirar numeros repetidos para poder fazer a contagem da saída'''
    lista_sem_repeticao = []
    for i in lista:
        if i not in lista_sem_repeticao:
            lista_sem_repeticao.append(i)
    return lista_sem_repeticao

def ordenar_crescente(lista):
    '''Função para ordenar uma lista em ordem crescente'''
    for i in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux
    return lista

def ordenar_probabilidade(lista,lista2):
    '''Função para ordenar uma lista em função da outra'''
    for i in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista2[i] > lista2[i + 1]:
                aux = lista2[i]
                aux2 = lista[i]
                lista2[i] = lista2[i + 1]
                lista2[i + 1] = aux
                lista[i] = lista[i + 1]
                lista[i + 1] = aux2


def devolver_lista(lista):
     '''Função para devolver a saída da lista em ordem de probabilidade'''
    for i in lista:
        print(i, end=' ')


def main():
    lista_entrada = input().split()
    lista_entrada = inteirar(lista_entrada)
    maior = maior_da_lista(lista_entrada)
    frequencia = contar_frequencia(lista_entrada,maior)
    frequencia_sem_zeros = tirar_zeros(frequencia)
    lista_sem_repeticao = tirar_repeticao(lista_entrada)
    lista_ordem = ordenar_crescente(lista_sem_repeticao)
    ordenar_probabilidade(lista_ordem,frequencia_sem_zeros)
    devolver_lista(lista_sem_repeticao)
main()