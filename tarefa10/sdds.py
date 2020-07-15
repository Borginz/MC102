imagem = [[] for _ in range(altura)]
    imagem_codificacao = []
    for i in range(0,codificacao,2):
        imagem_codificacao.append(codificacao[i])
    multiplicador = 0
    for k in range(0,altura,2):
        for j in range(largura):
            imagem[k].append((imagem_codificacao[multiplicador*largura + j][0]))
            imagem[k+1].append((imagem_codificacao[multiplicador*largura + j][1]))
        multiplicador+=1
    return imagem