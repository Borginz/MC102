def codificar(largura, altura, imagem):
    lista_codificacao = []
    for g in range(0, altura, 2):
        for w in range(largura):
            lista_codificacao.append(imagem[g][w] + imagem[g + 1][w])
    padrao = lista_codificacao[0]
    codificacao = []
    contagem = 0
    for i in range(len(lista_codificacao)):
        if lista_codificacao[i] == padrao:
            if i == len(lista_codificacao) - 1:
                if lista_codificacao[i] == padrao:
                    contagem += 1
                    codificacao.append(contagem)
                    codificacao.append(padrao)
                else:
                    codificacao.append(contagem)
                    codificacao.append(padrao)
                    contagem = 1
                    padrao = lista_codificacao[i]
                    codificacao.append(contagem)
                    codificacao.append(padrao)
            else:
                contagem += 1
        else:
            codificacao.append(contagem)
            codificacao.append(padrao)
            contagem = 1
            padrao = lista_codificacao[i]

    return lista_codificacao, codificacao








def decodificar(largura, altura, codificacao):
    imagem = [[] for _ in range(altura)]
    imagem_codificacao = []
    for i in range(0, len(codificacao), 2):
        for _ in range(codificacao[i]):
            imagem_codificacao.append(codificacao[i + 1])
    multiplicador = 0
    for k in range(0, altura, 2):
        for j in range(largura):
            imagem[k].append(str(imagem_codificacao[(multiplicador * largura) + j][0]))
            imagem[k + 1].append(str(imagem_codificacao[(multiplicador * largura) + j][1]))
        multiplicador += 1
    return imagem


def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        tipo_arquivo = arquivo.readline().strip()
        largura_altura = arquivo.readline().strip()
        imagem_codificada = arquivo.readline().strip()
    lista_larg_alt = largura_altura.split()
    largura = int(lista_larg_alt[0])
    altura = int(lista_larg_alt[1])
    return largura,altura,imagem_codificada


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
    with open(nome_do_arquivo, "w") as arquivo:
        print("P1C", file=arquivo)
        print(largura,altura, file=arquivo)
        print(codificacao, file=arquivo)

def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as arquivo:
        print("P1", file=arquivo)
        print(largura,altura, file=arquivo)
        for elemento in imagem:
            linha = elemento + "\n"
            arquivo.write(linha)
