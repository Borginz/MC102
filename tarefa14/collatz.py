
def collatz(n,contador):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return collatz(n/2,)
    else:
        return collatz((3*n+1)/2,contador)



def main():
    numero = int(input())
    contador = 0
    collatz(numero,contador)
    print(contador)
main()