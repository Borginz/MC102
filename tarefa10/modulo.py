def codificar(largura, altura, imagem):
    return codificacao


def decodificar(largura, altura, codificacao):




    return imagem


def carregar_imagem_codificada(nome_do_arquivo):
    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    return largura, altura, imagem


def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        arquivo.write('P1C\n')
        arquivo.write(f'{largura} {altura}\n')
        arquivo.write(f'{codificacao}\n')



def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, 'w') as arquivo:
        arquivo.write(f'P1C\n')
        arquivo.write(f'{largura} {altura}\n')
        for idx_linha in range(altura):
            for elemento in imagem[idx_linha]:
                if not idx_linha == altura-1:
                    arquivo.write(f'{elemento}')
                else:
                    arquivo.write(f'{elemento}\n')






def main():

    m, n, codificacao = carregar_imagem_codificada(input())
    imagem = decodificar(m, n, codificacao)
    nova_imagem = destacar_bordas(m, n, imagem)

    codificacao = codificar(m, n, nova_imagem)
    escrever_imagem_codificada(m, n, codificacao, input())


if __name__ == '__main__':
    main()