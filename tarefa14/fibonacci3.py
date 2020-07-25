def achar_enesimo(n,dict):
    if 0<=n<=2:
        dict[n] = n
    else:
        if n-3 not in dict.values():
            dict[n-3]= achar_enesimo(n-3,dict)
        else:
            return







def main():
    numero = int(input())
    dicionario = dict()
    (achar_enesimo(numero,dicionario))
    print(dicionario[numero])

main()


