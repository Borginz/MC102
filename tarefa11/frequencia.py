def ler_entrada():
    arquivo_txt = input()
    stop_words = input().strip()
    return arquivo_txt, stop_words


def ler_arquivo(nome_do_arquivo):
    texto = []
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavras = linha.strip().split()
            for idx in range(len(palavras)):
                texto.append(palavras[idx])
    return texto


def filtrar_texto(texto, stop_words):
    texto_sem_stop = []
    for palavra in texto:
        if palavra not in stop_words:
            texto_sem_stop.append(palavra)
    texto_filtrado = []
    for palavras in texto_sem_stop:
        palavra_certa = remover_pontuacao(palavras)
        palavra_certa = palavra_certa.lower()
        texto_filtrado.append(palavra_certa)
    return texto_filtrado


def contar_frequencia(texto):
    freq = dict()
    for chave in texto:
        if chave not in freq:
            freq[chave] = 1
        else:
            freq[chave] += 1
    return freq


def freq_individual(palavra, texto):
    contagem = 0
    for outras in texto:
        if outras == palavra:
            contagem += 1
    return contagem


def ordenar_frequencia(dict_frequencia):
    dict_frequencia.sort(key=lambda x: x[0], reverse=True)
    dict_frequencia.append((0, "palavra0"))
    contador = 0
    for k in range(len(lista_frequencia) - 1):
        if lista_frequencia[k][1] != lista_frequencia[k + 1][1]:
            lista_frequencia[contador:k + 1] = sorted(lista_frequencia[contador:k + 1])
            contador = k + 1
    lista_frequencia.remove((0, "palavra0"))
    print("lista_frequencia =", lista_frequencia)
    return lista_frequencia


def pegar_frequentes(lista):
    return [lista[0][1], lista[2][1], lista[3][1]]


def obter_do_quartil(lista):
    lista_quartil = []
    for idx in range(len(lista)):
        if lista[idx][0] >= 5:
            lista_quartil.append(lista[idx][0])
        else:
            break
    return lista_quartil


def calcular_frequencia_quartil(lista):
    idx = len(lista) // 4 - 1
    contador = 0
    for k in range(len(lista)):
        if lista[k][0] >= lista[idx][0]:
            contador += 1
        else:
            break
    return contador


def contar_alem(lista, x):
    return [lista[x][1], lista[x + 1][1], lista[x + 2][1]]


def mostrar_saida(palavras_frequentes, maiores_quartil, palavras_alem):
    for palavra in palavras_frequentes:
        print(palavra, end=' ')
    print(maiores_quartil)
    for palavra_alem in palavras_alem:
        print(palavra_alem, end=' ')


def remover_pontuacao(palavra):
    pontuacao = ",.;:?!''"
    palavra_certa = ""
    for letras in palavra:
        if letras not in pontuacao:
            palavra_certa += letras
    return palavra_certa


def main():
    arquivo, stop_words = ler_entrada()
    texto = ler_arquivo(arquivo)
    texto_filtrado = filtrar_texto(texto, stop_words)
    dict_frequencia = contar_frequencia(texto_filtrado)
    lista_ordem = ordenar_frequencia(dict_frequencia)
    palavras_frequentes = pegar_frequentes(lista_ordem)
    maiores_quartil = obter_do_quartil(lista_ordem)
    frequencia_quartil = calcular_frequencia_quartil(lista_ordem)
    palavras_alem = contar_alem(lista_ordem, frequencia_quartil)
    mostrar_saida(palavras_frequentes, maiores_quartil, palavras_alem)


main()

'''def ordenar_frequencia(dict_frequencia):
    dict_frequencia.sort(key=lambda x: x[0], reverse=True)
    dict_frequencia.append((0, "palavra0"))
    contador = 0
    for k in range(len(lista_frequencia) - 1):
        if lista_frequencia[k][1] != lista_frequencia[k + 1][1]:
            lista_frequencia[contador:k + 1] = sorted(lista_frequencia[contador:k + 1])
            contador = k + 1
    lista_frequencia.remove((0, "palavra0"))
    print("lista_frequencia =", lista_frequencia)
    return lista_frequencia'''

