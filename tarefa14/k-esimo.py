def achar_menor(lista,n):
    if n == 1:
        return min(lista)
    else:
        lista.remove(min(lista))
        return achar_menor(lista,n-1)





def main():
    lista = [int(x) for x in input().split()]
    n = int(input())
    n = achar_menor(lista,n)
    print(n)
main()