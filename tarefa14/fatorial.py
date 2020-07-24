def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*fatorial(num-1)

def main():
    num = int(input())
    print(fatorial(num))
main()