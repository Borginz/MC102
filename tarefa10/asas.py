altura = 6
largura = 8
codificacao = [4,'01',4,'00',8,'11']

imagem = [[] for _ in range(altura)]
imagem_codificacao = []
for p in range(0, len(codificacao), 2):
    for _ in range(codificacao[p]):
        imagem_codificacao.append(codificacao[p + 1])
print(imagem_codificacao)

i = 0
l = 0

while i < (altura-1):
    for j in range(largura):
        imagem[i].append(str(imagem_codificacao[(l*largura)+j][0]))
        imagem[i+1].append(str(imagem_codificacao[(l*largura)+j][1]))
        i+=2
        l+=1

print(imagem)