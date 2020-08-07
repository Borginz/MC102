


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
            contador+1
            if idx_linear == len(imagem_linear)-1:
                codificacao.append(str(contador))
                codificacao.append(padrao)
        else:
            codificacao.append(str(contador))
            codificacao.append(padrao)
            padrao = imagem_linear[idx_linear]
            contador = 1


    return codificacao
def main():
    largura = 6
    altura = 8
