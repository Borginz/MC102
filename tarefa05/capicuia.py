n = input()
nint = int(n)
if nint <100 and n[0] == n[-1]:
    print('sim')
elif nint>=100 and nint<1000 and n[0] == n[-1]:
    print('sim')
elif nint>= 100 and nint<10000 and n[0] == n[-1] and n[1] ==n[-2]:
    print('sim')
else:
    print('não')




















