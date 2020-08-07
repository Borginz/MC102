from modulo import *

def destacar_bordas(largura,altura,imagem):
    nova_imagem = []
    for idx_alt in range(altura):
        for idx_larg in range(largura):
            nova_imagem.append(imagem[idx_alt][idx_larg])
    for i in range(1,altura-1):
        for j in range(1,largura-1):
            if nova_imagem[i][j] == '1':
                if imagem[i][j-1] == '0' or imagem[i][j+1] == '0' or imagem[i+1][j] == '0' or imagem[i+1][j-1] == '0' or imagem[i+1][j+1] or imagem[i-1][j] == '0' or imagem[i-1][j+1] == '0' or imagem[i-1][j-1] == '0':
                    imagem[i][j] = '1'
                else:
                    imagem[i][j] = '0'


    return imagem







def main():

    m, n, codificacao = carregar_imagem_codificada(input())
    imagem = decodificar(m, n, codificacao)
    nova_imagem = destacar_bordas(m, n, imagem)

    codificacao = codificar(m, n, nova_imagem)
    escrever_imagem_codificada(m, n, codificacao, input())


if __name__ == '__main__':
    main()