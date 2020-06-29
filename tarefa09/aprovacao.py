
def separar_notas(notas):
    '''Função para pegar uma lista de tarefas com as notas e separar as
    ultimas adicionando-as em uma segunda lista de apenas notas'''
    lista_notas = []
    for i in range(len(notas)):
        if not i % 2 == 0:
            lista_notas.append(notas[i])
    return lista_notas
def aprovado_notas(notas):
    '''Função para verificar pela lista de notas se o aluno esta aprovado
    nesse quesito'''
    aprovado_notas = True
    for i in notas:
        if i == 'D':
            aprovado_notas = False
            break
    return aprovado_notas
def aprovado_frequencia(frequencia,lista):
    '''Função para verificar pela frequencia se o aluno esta aprovado
    no critério presença, analisando as presenças sobre o numero total de
    aulas(que é o tamanho da lista da chamada)'''
    aprovado_frequencia = True
    numero_de_aulas = len(lista)
    for presença in frequencia:
        if presença/numero_de_aulas >= 0.75:
            aprovado_frequencia = True
        else:
            aprovado_frequencia = False
    return aprovado_frequencia

def anotar_frequencia():
    ''' Função para receber linha por linha a ausencia ou nao do aluno
    e adicionar numma lista de chamada'''
    lista_chamada = []
    while True:
        try:
            chamada = input()
            lista_chamada.append(chamada)
        except EOFError:
            break
    return lista_chamada

def contar_frequencia(lista):
    ''' Função para contar quantas vezes o aluno esteve presente numa lista
    frequencia'''
    frequencia = [0]
    for i in lista:
        if i == 'presente':
            frequencia[0]+= 1
    return frequencia

def aprovacao(notas, frequencia):
    '''Função para devolver a saída correspondente aos critérios de notas e presença'''
    if notas and frequencia:
        print('Aprovadx')
    else:
        print('Reprovadx')


def main():
    entrada_notas = input().split()
    lista_chamada = anotar_frequencia()
    lista_frequencia = contar_frequencia(lista_chamada)
    lista_notas = separar_notas(entrada_notas)
    notas = aprovado_notas(lista_notas)
    frequencia = aprovado_frequencia(lista_frequencia, lista_chamada)
    aprovacao(notas, frequencia)


main()
