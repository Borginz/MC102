def maior_L(L):
    n = 0
    for i in L:
        i = int(i)
        if i > n:
            n = i
    return n
def inteirar(L):
    for i in L:
        i = int(i)
    return L
def contar_frequencia(L,n):
    F = [0] * (n + 1)
    for i in L:
        i = int(i)
        F[i] += 1
    return F
def tirar_zeros(F):
    F2 = []
    for i in F:
        if i != 0:
            F2.append(i)
    return F2
def tirar_repeticao(L):
    L2 = []
    for i in L:
        if i not in L2:
            L2.append(i)
    return L2
def ordenar_crescente(L2):
    for i in range(len(L2) - 1):
        for i in range(len(L2) - 1):
            if L2[i] > L2[i + 1]:
                aux = L2[i]
                L2[i] = L2[i + 1]
                L2[i + 1] = aux
def ordenar_ocorrencias(L2,F2):
    for j in range(len(L2)-1):
        for w in range(len(F2)-1):
            for i in range(len(F2)-1):
                if F2[i] > F2[i+1]:
                    aux = F2[i]
                    aux2 = L2[i]
                    F2[i] = F2[i+1]
                    F2[i+1]= aux
                    L2[i] = L2[i+1]
                    L2[i+1] = aux2
def devolver_L(L2):
    for i in L2:
        print(i, end=' ')


def main():
    L = input().split()
    L = inteirar(L)
    n = maior_L(L)
    F = contar_frequencia(L,n)
    F2 = tirar_zeros(F)
    L2 = tirar_repeticao(L)
    ordenar_crescente(L2)
    ordenar_ocorrencias(L2,F2)
    devolver_L(L2)
main()