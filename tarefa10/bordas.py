from modulo import *


def destacar_bordas(largura,altura,imagem):
    nova_imagem = []
    for linha in imagem:
        nova_imagem.append(linha[:])
    for i in range(1,altura-1):
        for j in range(1,largura-1):
            if imagem[i][j] == '1':
                if imagem[i-1][j-1] == '1' and imagem[i-1][j] == '1' and imagem[i-1][j+1] == '1' and \
                        imagem[i][j] == '1' and imagem[i][j+1] == '1' and \
                        imagem[i+1][j] == '1' and imagem[i+1][j+1] == '1' and imagem[i+1][j-1] == '1':
                    nova_imagem[i][j] = '0'

    return nova_imagem







def main():

    m, n, codificacao = carregar_imagem_codificada(input())
    imagem = decodificar(m, n, codificacao)
    nova_imagem = destacar_bordas(m, n, imagem)

    codificacao = codificar(m, n, nova_imagem)
    escrever_imagem_codificada(m, n, codificacao, input())


if __name__ == '__main__':
    main()