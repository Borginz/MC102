#programa dos triangulos

a = float(input())
b = float(input())
c = float(input())
if a>b and a>c:
    if a**2==b**2+c**2:
        print('retângulo')
        if a**2<b**2+c**2:
            print ('acutangulo')
        if a**2>b**2+c**2:
            print ('obtusângulo')
        else:
            print('não é triangulo')
if b>a and b>c:
    if b**2==a**2+c**2:
        print('retângulo')
        if b**2<a**2+c**2:
            print ('acutangulo')
        if b**2>a**2+c**2:
            print ('obtusângulo')
        else:
            print('não é triangulo')
if c>=a and c>=b:
    if c**2==b**2+a**2:
        print('retângulo')
        if c**2<b**2+a**2:
            print ('acutangulo')
        if c**2>b**2+a**2:
            print ('obtusângulo')
