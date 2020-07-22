def ler_entrada():
    arquivo_txt = input()
    stop_words = input().split()
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
    texto_filtrado = []
    for palavras in texto:
        palavras = palavras.lower()
        palavra_certa = remover_pontuacao(palavras)
        texto_filtrado.append(palavra_certa)
    for palavra in texto_filtrado:
        if palavra not in stop_words:
            texto_sem_stop.append(palavra)

    return texto_sem_stop


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
    tuplas.sort(key=lambda x: x[0])
    tuplas.sort(key=lambda x: x[1], reverse=True)
    return tuplas


def pegar_frequentes(tuplas):
    return [tuplas[0][0], tuplas[1][0], tuplas[2][0]]


def obter_do_quartil(tupla):
    lista_quartil = []
    for idx in range(len(tupla)):
        if tupla[idx][1] > 5:
            lista_quartil.append(tupla[idx])
        else:
            break
    return lista_quartil


def calcular_frequencia_quartil(tupla):
    n = len(tupla)
    Q1 = round(0.25 * (n + 1))
    pos_quartil = tupla[Q1:]
    idx = Q1
    for k in range(len(pos_quartil)):
        if pos_quartil[k][1] == tupla[Q1 - 1][1]:
            idx += 1
        else:
            break
    return idx


def contar_alem(lista, x):
    return [lista[x][0], lista[x + 1][0], lista[x + 2][0]]


def mostrar_saida(palavras_frequentes, maiores_quartil, palavras_alem):
    for palavra in palavras_frequentes:
        print(palavra, end=' ')
    print()
    print(maiores_quartil)
    for palavra_alem in palavras_alem:
        print(palavra_alem, end=' ')
    print()


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
    tuplas_quartil = obter_do_quartil(tuplas_ordem)
    frequencia_quartil = calcular_frequencia_quartil(tuplas_quartil)
    palavras_alem = contar_alem(tuplas_quartil, frequencia_quartil)
    mostrar_saida(palavras_frequentes, frequencia_quartil, palavras_alem)

