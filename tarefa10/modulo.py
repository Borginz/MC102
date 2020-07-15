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
    for i in range(0,codificacao,2):
        for _ in range(codificacao[i]):
            imagem_codificacao.append(codificacao[k+1])
    multiplicador = 0
    for k in range(0,altura,2):
        for j in range(largura):
            imagem[k].append(imagem_codificacao[multiplicador*largura+j][0])
            imagem[k+1].append(imagem_codificacao[multiplicador*largura+j][1])
        multiplicador+=1
    return imagem
















    return imagem








def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        P1C = arquivo.readline()
        largura_altura = arquivo.readline().split()
        largura = largura_altura[0]
        altura = largura_altura[1]
        codificacao = arquivo.readline()
    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        imagem = []
        for linha in arquivo:
            linhas = linha.strip()
            imagem.append(linhas)
            altura = len(imagem)
            largura = len(imagem[0])
    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    with open(nome_do_arquivo, "w" ) as arquivo:
        print("P1C")
        print(largura,altura)
        print(codificacao)

def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as arquivo:
        print("P1")
        print(largura,altura)
        for elemento in imagem:
            linha = elemento + "\n"
            arquivo.write(linha)







