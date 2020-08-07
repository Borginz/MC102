from modulo import carregar_imagem_codificada, decodificar, codificar, escrever_imagem_codificada

def destacar_bordas(largura,altura,imagem):



    return imagem







def main():

    m, n, codificacao = carregar_imagem_codificada(input())
    imagem = decodificar(m, n, codificacao)
    nova_imagem = destacar_bordas(m, n, imagem)

    codificacao = codificar(m, n, nova_imagem)
    escrever_imagem_codificada(m, n, codificacao, input())


if __name__ == '__main__':
    main()