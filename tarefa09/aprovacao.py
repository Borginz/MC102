
def separar_notas(notas):
    '''Pegar a lista de entrada e anotar apenas as notas para analisar'''
    lista_notas = []
    for i in range(len(notas)):
        if not i % 2 == 0:
            lista_notas.append(notas[i])
    return lista_notas
def aprovado_notas(notas):
    '''Fazer a analise referente as notas dos alunos'''
    aprovado_notas = True
    for i in notas:
        if i == 'D':
            aprovado_notas = False
    return aprovado_notas
def aprovado_frequencia(frequencia,lista):
    '''Esta função ira comparar a L[0]/len(lista) >= 0.75
    '''





def anotar_frequencia():
    ''' Função para receber por linha a frequencia do aluno na escola '''
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
    '''função para devovler a saída em relaçao as notas e frequencias'''
    if notas and frequencia == True:
        return ('Aprovadx')
    else:
        return ('Reprovadx')




def main():
    entrada_notas = input(' digite as tarefas com notas ').split()
    lista_chamada = anotar_frequencia()
    lista_frequencia = contar_frequencia(lista_chamada)
    lista_notas = separar_notas(entrada_notas)
    notas = aprovado_notas(lista_notas)
    frequencia = aprovado_frequencia(entrada_frequencia, lista_frequencia)
    print(aprovacao(notas, frequencia))


main()
