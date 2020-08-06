def codificar(largura, altura, imagem):
    '''padraoi == imagem[]
    codificacao = []
    for idx in range(0,altura,2):
        for codificacoes in range(largura):
            decodificacao.append(imagem[idx][codificacoes]+imagem[idx][codificacoes])
    for idx i'''




    '''return codificacao'''
def main():
    largura = 8
    altura = 6
    imagem = [['0','0','0','0','0','0','0','0'],
              ['1','1','1','1','0','0','0','0'],
              ['1','1','1','1','1','1','1','1'],
              ['1','1','1','1','1','1','1','1'],
              ['1','1','1','1','1','1','1','1'],
              ['1','1','1','1','1','1','1','1']]
    codificacao = codificar(largura,altura,imagem)
    print(imagem)
    print(codificacao)
main()