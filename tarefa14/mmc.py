
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    mmc = a*b//(mdc(a,b))
    print(mmc)

main()

