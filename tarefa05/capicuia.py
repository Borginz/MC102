n = int((input('digite um numero ')))
if n > 0:
    n = str(n)
    if len(n) < 5:
        if len(n) == 1:
            print('sim')
        elif len(n) <= 4 and n[0] == n[-1] and n[1] == n[-2]:
            print('sim')
        else:
            print('não')




















