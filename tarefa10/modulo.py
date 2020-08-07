def codificar(largura, altura, imagem):
    codificacao = []
    imagem_linear = []
    for idx_alt in range(0,altura,2):
        for idx_larg in range(largura):
            imagem_linear.append(imagem[idx_alt][idx_larg]+imagem[idx_alt+1][idx_larg])
    padrao = imagem_linear[0]
    contador = 0
    for idx_linear in range(len(imagem_linear)):
        if imagem_linear[idx_linear] == padrao:
            if idx_linear == len(imagem_linear)-1:
                contador += 1
                codificacao.append(str(contador))
                codificacao.append(padrao)
            else:
                contador += 1
        else:
            codificacao.append(str(contador))
            codificacao.append(padrao)
            padrao = imagem_linear[idx_linear]
            contador = 1


    return codificacao


def decodificar(largura, altura, codificacao):
    imagem = [[] for _ in range(altura)]
    imagem_decodificada = []
    for idx_freq in range(0,len(codificacao),2):
        for freq in range(int(codificacao[idx_freq])):
            imagem_decodificada.append(codificacao[idx_freq+1])
    contador = 0
    for idx_linha in range(0,altura,2):
        for idx_coluna in range(largura):
            imagem[idx_linha].append(str(imagem_decodificada[(contador*largura)+idx_coluna][0]))
            imagem[idx_linha+1].append(str(imagem_decodificada[(contador*largura)+idx_coluna][1]))
        contador += 1
    return imagem

def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        arquivo.readline()
        larg_alt = arquivo.readline().strip()
        largura,altura = larg_alt.split()
        largura = int(largura)
        altura = int(altura)
        codificacao = arquivo.readline().strip().split()

    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    imagem = []
    with open(nome_do_arquivo) as arquivo:
        arquivo.readline()
        largura,altura = arquivo.readline().strip().split()
        largura = int(largura)
        altura = int(altura)
        cont_linha = 0
        while cont_linha != altura:
            linha = arquivo.readline().strip()
            imagem.append([])
            for elemento in linha:
                imagem[cont_linha].append(elemento)
            cont_linha += 1


    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        arquivo.write('P1C\n')
        arquivo.write(largura+' '+altura+'\n')
        for elementos in codificacao:
            print(elementos,end=' ',file=arquivo)



def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        arquivo.write(f'P1C\n')
        arquivo.write(largura+' '+altura+'\n')
        for idx_linha in range(altura):
            for idx in range(largura):
                if not idx == altura-1:
                    arquivo.write(imagem[idx_linha][idx])
                else:
                    arquivo.write(imagem[idx_linha][idx]+'\n')