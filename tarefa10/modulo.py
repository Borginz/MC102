def codificar(largura, altura, imagem):
    padraoi == imagem[0][0]
    padraoj == imagem[1][0]
    codificacao = []
    for idx in range(0,altura,2):
        for codificacoes in range(largura):
            decodificacao.append(imagem[idx][codificacoes]+imagem[idx][codificacoes])
    for idx i




    return codificacao


def decodificar(largura, altura, codificacao):
    imagem_decodificada = []
    imagem = [[] for _ in range(altura)]




    return imagem


def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        P1C = arquivo.readline().strip()
        larg_alt = arquivo.readline().strip()
        codificacao = arquivo.readline().strip().split()
        altura,largura = larg_alt.split()
        altura = int(altura)
        largura = int(largura)


    return largura, altura, codificacao


def carregar_imagem_decodificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        P1C = arquivo.readline().strip()
        larg_alt = arquivo.readline().strip()
        altura, largura = larg_alt.split()
        altura = int(altura)
        largura = int(largura)
        imagem = []
        cont_linha = 0
        idx_coluna = 0
        while cont_linha < altura:
            linha = arquivo.readline().strip()
            imagem.append([])
            while idx_coluna < largura:
                imagem[cont_linha].append(linha[idx_coluna])
                idx_coluna+=1
        cont_linha+=1




#for elemento in linha:
#imagem[cont_linha].append(elemento)
#cont_linha+=1





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