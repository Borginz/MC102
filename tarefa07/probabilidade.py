def tirar_repeticao(lista):
    """Função para deixar apenas os eventos unicos"""
    lista2 = []
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    return lista2

def contar_frequencia(lista,lista2):
    """Função para contar a frequencia dos eventos unicos na lista de entrada"""
    frequencia = [0]*len(lista2)
    for i in range(len(lista2)):
        for j in lista:
            if lista2[i] == j:
                frequencia[i]+=1
    return frequencia

def ordenar_listas(lista,lista2):
    """Função para organizar a freequencia com os eventos unicos"""
    for i in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista2[i] > lista2[i+1]:
                aux = lista2[i]
                aux2 = lista[i]
                lista2[i] = lista2[i+1]
                lista2[i+1] = aux
                lista[i] = lista[i+1]
                lista[i+1] = aux2
def devolver_lista(lista):
    """Função para devolver separado pos espaços a lista"""
    for i in lista:
        print(i,end=' ')

def main():
    lista_entrada = [int(x) for x in input().split()]
    lista_sem_repeticao = tirar_repeticao(lista_entrada)
    frequencia = contar_frequencia(lista_entrada, lista_sem_repeticao)
    ordenar_listas(lista_sem_repeticao, frequencia)
    devolver_lista(lista_sem_repeticao)
main()