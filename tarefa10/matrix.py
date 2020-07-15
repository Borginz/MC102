def codificar(largura, altura, imagem):
    codificacao = []
    padrao = imagem[0][0] + imagem[1][0]
    contagem = 0
    for i in range(0,altura,2):
        for k in range(largura):
            if imagem[i][k]+imagem[i+1][k] == padrao:
                if k == largura-1 and i < altura-2:
                    if imagem[i][k]+imagem[i+1][k] == imagem[i+2][k]+imagem[i+3][k]:
                        codificacao.append(contagem)
                        codificacao.append(padrao)
                        padrao = imagem[i+2][k]+imagem[i+3][k]
                        contagem = 0
                else:
                    contagem += 1




            else:
                codificacao.append(contagem)
                codificacao.append(padrao)
                contagem = 1
                padrao = imagem[i][k]+imagem[i+1][k]
    return codificacao
def decodificar(largura, altura, codificacao):
    imagem = []
    imagem.append([])
    contagem = 0

    for i in range(altura-1):


















def main():
    largura = 8
    altura = 6
    imagem = [['0', '0', '0', '0', '0', '0', '0', '0'], ['1', '1', '1', '1', '0', '0', '0', '0'], ['1', '1', '1', '1', '1', '1', '1', '1'],
              ['1', '1', '1', '1', '1', '1', '1', '1'], ['1', '1', '1', '1','1','1', '1', '1'], ['1', '1', '1', '1', '1', '1', '1', '1']]
    codificação = codificar(largura,altura,imagem)
    print(''.join(codificação)

main()
































'''def codificar(largura, altura, imagem):
    codificacao = []
    for i in range(0,altura,2):
        for j in range(1,altura,2):
            for elmnt_impar in imagem[i]:
                for elmnt_par in imagem[j]:
                    padrao = elmnt_impar+elmnt_par
                    contagem = 0
                    if elmnt_impar+elmnt_par == padrao:
                        contagem+=1
                    else:
                        codificacao.append(padrao,contagem)
                        padrao = elmnt_impar+elmnt_par
                        contagem = 0
    return codificacao


def main():
        altura = 6
        largura = 8
        imagem = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
        codificacao = codificar(largura, altura, imagem)
        print(codificacao)
main()'''
