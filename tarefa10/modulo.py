def codificar(largura, altura, imagem):
    codificacao = []
    for i in range(0,altura,2):
        for k in range(largura):
            padrao = imagem[i][k]+imagem[i+1][k]
            contagem = 0
            if imagem[i][k]+imagem[i+1][k] == padrao:
                if not  k == largura-1:
                    contagem += 1
                elif k == largura-1:




def decodificar(largura, altura, codificacao):
    imagem = []
    imagem.append([] * largura)
    for i in range(altura-1):
        imagem.append(imagem[0])





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







