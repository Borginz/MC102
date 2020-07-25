def busca(lista,n,min,max):
    if min > max:
        return -1
    meio = (min+max)//2
    if n == lista[meio]:
        return meio
    elif n > lista[meio]:
        return busca(lista,n,meio+1,max)
    else:
        return busca(lista,n,min,meio-1)




def main():
    lista = [int(x) for x in input().split()]
    numero = int(input())
    vetor = busca(lista,numero,0,len(lista)-1)
    print(vetor)
main()