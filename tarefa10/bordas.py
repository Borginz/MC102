from modulo import *


def destacar_bordas(largura, altura, imagem):
    nova_imagem = []
    for _ in range(altura):
        nova_imagem.append([])
    for i in range(altura):
        for j in range(largura):
            if i == 0 or j == 0 or i == altura - 1 or j == largura - 1:
                nova_imagem[i].append(imagem[i][j])
            else:
                if imagem[i][j] == '1':
                    if imagem[i-1][j] == '0' or imagem[i+1][j] == '0' or imagem[i][j-1] == '0' or imagem[i][j+1] == '0' or imagem[i+1][j+1] == '0' or imagem[i+1][j-1] == '0' or imagem[i-1][j+1] == '0' or imagem[i-1][j-1] == '0':
                        nova_imagem[i].append('1')
                    else:
                        nova_imagem[i].append('0')
                else:
                    nova_imagem[i].append('0')
    return nova_imagem


def main():

    arquivo_entrada = input()
    arquivo_saida = input()

    largura, altura, codificacao = carregar_imagem_codificada(arquivo_entrada)
    imagem = decodificar(largura, altura, codificacao)
    nova_imagem = destacar_bordas(largura, altura, imagem)

    codificacao = codificar(largura, altura, nova_imagem)
    escrever_imagem_codificada(largura, altura, codificacao, arquivo_saida)


if __name__ == '__main__':
    main()


  