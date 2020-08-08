def destacar_bordas(largura,altura,imagem):
    nova_imagem = imagem[:]
    for i in range(1,altura-1):
        for j in range(1,largura-1):
            if imagem[i][j] == '1':
                if imagem[i][j-1] == '0' or imagem[i][j+1] == '0' or imagem[i+1][j] == '0' or imagem[i+1][j-1] == '0' \
                        or imagem[i+1][j+1] or imagem[i-1][j] == '0' or imagem[i-1][j+1] == '0' or imagem[i-1][j-1] == '0':
                    nova_imagem[i][j] = '1'
                else:
                    nova_imagem[i][j] = '0'
    print(nova_imagem)
    return nova_imagem
def