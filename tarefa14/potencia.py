def potencia(a,b):
    if b == 0:
        return 1
    else:
        return a*potencia(a,b-1)


def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(potencia(a,b))
main()