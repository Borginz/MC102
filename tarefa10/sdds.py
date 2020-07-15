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

main()