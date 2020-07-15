def codificar(largura, altura, imagem):
    codificacao = []
    padrao = imagem[0][0] + imagem[1][0]
    contagem = 0
    for i in range(0, altura, 2):
        for k in range(largura):
            if imagem[i][k] + imagem[i + 1][k] == padrao:
                if k == largura - 1 and i < altura - 2:
                    if imagem[i][k] + imagem[i + 1][k] == imagem[i + 2][k] + imagem[i + 3][k]:
                        codificacao.append(contagem)
                        codificacao.append(padrao)
                        padrao = imagem[i + 2][k] + imagem[i + 3][k]
                        contagem = 0
                else:
                    contagem += 1




            else:
                codificacao.append(contagem)
                codificacao.append(padrao)
                contagem = 1
                padrao = imagem[i][k] + imagem[i + 1][k]
    return codificacao


def decodificar(largura, altura, codificacao):
    imagem = [[] for _ in range(altura)]
    imagem_codificacao = []
    for i in range(0, len(codificacao), 2):
        for _ in range(codificacao[i]):
            imagem_codificacao.append(codificacao[i + 1])
    multiplicador = 0
    for k in range(0, altura, 2):
        for j in range(largura):
            imagem[k].append(imagem_codificacao[(multiplicador * largura)+j][0])
            imagem[k+1].append(imagem_codificacao[(multiplicador * largura)+j][1])
        multiplicador += 1
    return imagem


def main():
    largura = 8
    altura = 6
    codificacao = [4,'01',4,'00',16,'11']
    print(decodificar(largura,altura,codificacao))
    imagem = [['0', '0', '0', '0', '0', '0', '0', '0'], ['1', '1', '1', '1', '0', '0', '0', '0'], ['1', '1', '1', '1', '1', '1', '1', '1'], ['1', '1', '1', '1', '1', '1', '1', '1'], ['1', '1', '1', '1', '1', '1', '1', '1'], ['1', '1', '1', '1', '1', '1', '1', '1']]
    print(codificar(largura,altura,imagem))
main()