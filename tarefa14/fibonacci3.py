def fibonaccizar(numero):
    if 0<=numero<=2:
        return numero
    else:
        numero = fibonaccizar(numero-1)+fibonaccizar(numero-2)+fibonaccizar(numero-3)
        return numero

def main():
    numero = int(input())
    print(fibonaccizar(numero))


main()