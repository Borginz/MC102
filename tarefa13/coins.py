notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
valor = float(input())
print("NOTAS:")
for nota in notas:
    nota_inteira = round(int(valor / nota - 0))
    if nota_inteira > 0:
        print(f"{nota_inteira} nota(s) de R$ {nota:.2f}")
        valor -= nota_inteira * nota

if valor !=0:
    print("MOEDAS:")
    for moeda in moedas:
        moeda_inteira = round(int(valor / moeda) - 0)
        if moeda_inteira > 0:
            print(f"{moeda_inteira} moeda(s) de R$ {moeda:.2f}")
            valor -= moeda_inteira * moeda






