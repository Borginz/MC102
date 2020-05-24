a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
# Agora vamos fazer as condicões para triangulos
#if abs(b-c)<a<b+c and abs(a-c)<b<a+c and abs(a-b)<c<a+b:
if a>b and a>c:
    if a<b+c and b<c+a and c< a+b:
        if a**2 == b**2+c**2:
            print('retângulo')
        elif a**2 < b**2+c**2:
            print('acutângulo')
        elif a**2 > b**2+c**2:
            print('obtusângulo')
    else:
        print ('não forma triângulo')
elif b>a and b>c:
    if a<b+c and b<c+a and c<a+b:
        if b**2 == a**2 + c**2:
            print('retângulo')
        elif b**2 < a**2 + c**2:
            print('acutângulo')
        elif b**2 < a**2 + c**2:
            print('obtusângulo')
    else:
        print('não forma triângulo')
elif c>=a and c>=b:
    if a<b+c and b<c+a and c<a+b:
        if c**2 == a**2+ b**2:
            print('retângulo')
        elif c**2 < a**2+ b**2:
            print('acutângulo')
        elif c**2 > a**2+ b**2:
            print('obtusângulo')
    else:
        print('não forma triângulo')











