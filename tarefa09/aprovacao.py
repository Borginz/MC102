
'''
Digite o numero de tarefas
Anote as notas pelo sistema par
escreva n vezes a quantidade de ida a escola
de a saída

'''
def separar_notas(notas):
    lista2 = []
    for i in range(len(notas)):
        if not i % 2 == 0:
            lista2.append(notas[i])
    return lista2
def aprovado_notas(notas):
    aprovado_notas = True
    for i in notas:
        if i == 'D':
            aprovado_notas = False
    return aprovado_notas
def aprovado_frequencia(frequencia,lista):
    '''Esta função ira comparar a L[1]/len(lista) >= 0.75
    '''
    n = len(frequencia)
    if lista[0]/n >= 0.75:
        return True
    else:
        return False


def anotar_frequencia():
    lista_chamada = []
    while True:
        try:
            chamada = input()
            lista_chamada.append(chamada)
        except EOFError:
            break
    return lista_chamada

def contar_frequencia(lista):
    '''Anota o tamanho da lista, para cada aprovadx ou reprovadx
    adiciona numa posição numa nova lista, se L[1]/len(lista)>= 0.75, aprovador
    caso contrario, reprovadx
    '''
    frequencia = [0,0]
    for i in lista:
        if i == 'presente':
            frequencia[0] += 1
        else:
            frequencia[1] += 1
    return frequencia





def aprovacao(notas, frequencia):
    if notas and frequencia == True:
        return ('Aprovadx')
    else:
        return ('Reprovadx')




def main():
    entrada_notas = input(' digite as tarefas com notas ').split()
    entrada_frequencia = anotar_frequencia()
    lista_frequencia = contar_frequencia(entrada_frequencia)
    notas = aprovado_notas(entrada_notas)
    frequencia = aprovado_frequencia(entrada_frequencia, lista_frequencia)
    print(aprovacao(notas, frequencia))


main()
