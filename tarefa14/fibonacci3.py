
def fib(n,dicio):
    if n <=2:
        return n
    if n in dicio:
        return dicio[n]
    else:
        numero = fib(n-1,dicio) + fib(n-2,dicio) + fib(n-3,dicio)
        dicio[n] = numero
        return numero

def main():
    n = int(input())
    dicio = {}
    print(fib(n,dicio))



main()
