'''  def codificar(largura, altura, imagem):
    lista_codificacao = []
    for g in range(0, altura, 2):
        for w in range(largura):
            lista_codificacao.append(imagem[g][w] + imagem[g + 1][w])
    padrao = lista_codificacao[0]
    codificacao = []
    contagem = 0
    for i in range(len(lista_codificacao)):
        if lista_codificacao[i] == padrao:
            if i == len(lista_codificacao) - 1:
                if lista_codificacao[i] == padrao:
                    contagem += 1
                    codificacao.append(contagem)
                    codificacao.append(padrao)
                else:
                    codificacao.append(contagem)
                    codificacao.append(padrao)
                    contagem = 1
                    padrao = lista_codificacao[i]
                    codificacao.append(contagem)
                    codificacao.append(padrao)
            else:
                contagem += 1
        else:
            codificacao.append(contagem)
            codificacao.append(padrao)
            contagem = 1
            padrao = lista_codificacao[i]

    return lista_codificacao, codificacao'''
''' novo'''
def codificar(largura, altura, imagem):
  idx=0
  lista_padroes=[]
  while idx < altura:
    for elementos in range(len(imagem[idx])):
      lista_padroes.append(imagem[idx][elementos]+imagem[idx+1][elementos])
    idx+=2
  codificacao=[]
  idx=0
  while idx<=len(lista_padroes)-1:
    soma=0
    for j in range(idx, len(lista_padroes)):
      if lista_padroes[idx]==lista_padroes[j]:
        soma+=1
        if j == len(lista_padroes)-1:
          codificacao.append(str(soma))
          codificacao.append(lista_padroes[idx])
          idx=j+1
          break
      else:
        codificacao.append(str(soma))
        codificacao.append(lista_padroes[idx])
        idx=j
        break

  return codificacao

def decodificar(largura, altura, codificacao):
    imagem = [[] for _ in range(altura)]
    imagem_codificacao = []
    for i in range(0, len(codificacao), 2):
        for _ in range(int(codificacao[i])):
            imagem_codificacao.append(codificacao[i + 1])
    multiplicador = 0
    for k in range(0, altura, 2):
        for j in range(largura):
            imagem[k].append(str(imagem_codificacao[(multiplicador * largura) + j][0]))
            imagem[k + 1].append(str(imagem_codificacao[(multiplicador * largura) + j][1]))
        multiplicador += 1
    return imagem

def carregar_imagem_codificada(nome_do_arquivo):
    with open(nome_do_arquivo) as arquivo:
        tipo_arquivo = arquivo.readline().strip()
        largura_altura = arquivo.readline().strip()
        imagem_codificada = arquivo.readline().strip().split()
    lista_larg_alt = largura_altura.split()
    largura = int(lista_larg_alt[0])
    altura = int(lista_larg_alt[1])
    return largura,altura,imagem_codificada

def carregar_imagem_decodificada(nome_do_arquivo):
    imagem = []
    with open(nome_do_arquivo) as arquivo:
        arquivo.readline()
        largura_altura = arquivo.readline().strip().split()
        largura = int(largura_altura[0])
        altura = int(largura_altura[1])
        for i in range(altura):
            linha = arquivo.readline().strip()
            imagem.append([])
            for num in linha:
                imagem[i].append(num)

    return largura, altura, imagem

'''def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
  with open(nome_do_arquivo, "w") as arquivo:
    tipo_arquivo="P1C\n"
    arquivo.write(tipo_arquivo)
    L = str(largura) + " "
    arquivo.write(L)
    H = str(altura) + "\n"
    arquivo.write(H)
    arquivo.writelines(" ".join(codificacao))'''
''' novo '''
def escrever_imagem_codificada(largura, altura, codificacao, nome_do_arquivo):
  with open(nome_do_arquivo, "w") as arquivo:
    tipo_arquivo="P1C\n"
    arquivo.write(tipo_arquivo)
    L = str(largura) + " "
    arquivo.write(L)
    H = str(altura) + "\n"
    arquivo.write(H)
    arquivo.writelines(" ".join(codificacao))

def escrever_imagem_decodificada(largura, altura, imagem, nome_do_arquivo):
    with open(nome_do_arquivo, "w") as arquivo:
        print("P1", file=arquivo)
        print(largura,altura, file=arquivo)
        for i in range(altura):
            for elemento in imagem[i]:
                arquivo.write(str(elemento))
            if i != (altura-1):
                arquivo.write("\n")


