''' como a quantidade de vezes é dada pela formula 2^64 - 1, podemos calcular
pela quantidade de vezes que a função é chamada menos 1'''
def quantidade(n):
    if n == 0:
        pass
    if n == 1:
        return 1
    else:
        return 2*quantidade(n-1)+1
def main():
    numero_discos = (int(input()))
    numero_mov = quantidade(numero_discos)
    print(numero_mov)

main()

