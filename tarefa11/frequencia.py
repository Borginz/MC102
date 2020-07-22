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

def ordenar_frequencia(dict):
    tuplas = []
    for k, v in dict.items():
        tuplas.append((k, v))
    tuplas.sort(key=lambda x: x[1], reverse=True)
    tuplas.append((0, "palavra0"))
    contador = 0
    for k in range(len(tuplas) - 1):
        if tuplas[k][0] != tuplas[k + 1][0]:
            tuplas[contador:k + 1] = sorted(tuplas[contador:k + 1])
            contador = k + 1
    tuplas.remove((0, "palavra0"))
    return tuplas




def pegar_frequentes(tuplas):
    return [tuplas[0][0], tuplas[1][0], tuplas[2][0]]


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
    tuplas_ordem = ordenar_frequencia(dict_frequencia)
    palavras_frequentes = pegar_frequentes(tuplas_ordem)
    print(palavras_frequentes)
    maiores_quartil = obter_do_quartil(tuplas_ordem)
    frequencia_quartil = calcular_frequencia_quartil(tuplas_ordem)
    palavras_alem = contar_alem(tuplas_ordem, frequencia_quartil)
    mostrar_saida(palavras_frequentes, maiores_quartil, palavras_alem)


main()


