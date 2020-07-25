def fibonaccizar(n,lista):
    if 0<=n<=2:
        return n
    else:
        n = fibonaccizar(lista[-1],lista)+fibonaccizar(lista[-2],lista)+fibonaccizar(lista[-3],lista)
        lista.append(n)
        return n

def main():
    numero = int(input())
    lista = [0,1,2]
    print(fibonaccizar(numero,lista))


main()