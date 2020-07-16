from modulo import *


def destacar_bordas(largura, altura, imagem):
    nova_imagem = [[] for _ in range(altura)]
    for k in range(altura):
        for u in range(largura):
            if k == 0 or k == altura-1 or u == 0 or u == largura-1:
                nova_imagem[k].append(imagem[k][u])
            else:
                if imagem[k][u] == '1':
                    if imagem[k+1][u] == '0' or imagem[k-1][u] == '0' or imagem[k][u+1] == '0' or imagem[k][u-1] == '0' or imagem[k+1][u+1] == '0' or imagem[k-1][u-1] == '0' or imagem[k+1][u-1] == '0' or imagem[k-1][u+1] == '0'
                        nova_imagem[k].append('1')
                    else:
                        nova_imagem[k].append('0')
                else:
                    nova_imagem[k].append('0')
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
  