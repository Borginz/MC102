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
    imagem = []
    for _ in range(altura):
        l = [] # linha começa vazia
        for _ in range(largura):
            l.append(" ")#preenche colunas da linha
        imagem.append(l)
    indice = 0
    contador = 0
    for i in range(0,altura,2):
        for k in range(largura):
            if contador < codificacao[indice]:
                imagem[i][k] = codificacao[indice+1][0]
                imagem[i+1][k] = codificacao[indice+1][1]
                contador+=1
            else:














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







