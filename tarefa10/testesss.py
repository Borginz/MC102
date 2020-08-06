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
            padrao = imagem_linear[idx_linear+1]
            contador = 1











    return codificacao,imagem_linear
def main():
    largura = 8
    altura = 6
    imagem = [['0','0','0','0','0','0','0','0'],['1','1','1','1','0','0','0','0'],['1','1','1','1','1','1','1','1'],['1','1','1','1','1','1','1','1'],['1','1','1','1','1','1','1','1'],['1','1','1','1','1','1','1','1']]
    codificacao,imagem = codificar(largura,altura,imagem)
    print(imagem)
    print(codificacao)
main()
