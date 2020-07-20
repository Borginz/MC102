def ler_entrada():
    arquivo_txt = input()
    stop_words = input().strip()
    return arquivo_txt, stop_words

def ler_arquivo(nome_do_arquivo):
    texto = []
    with open(nome_do_arquivo, 'r', encoding='utf-8'):
        for linha in arquivo:
            palavras = linha.strip().splip()
            for idx in range(len(palavras)):
                texto.append(palavras[idx])
def filtrar_texto(texto, stop_words):
    texto_sem_stop = []
    texto_filtrado = []
    pontuacao = ['!','!\n','?',' ?\n','.\n',',','.',':','"',';']
    for palavra in texto:
        if palavra not in stop_words:
            texto_sem_stop.append(texto_filtrado)
    for filtrada in texto_sem_stop:
        if filtrada not in texto_sem_stop:
            texto_filtrado.append(filtrada)
    return texto_filtrado

def contar_frequencia(texto):
    frequencia = []
    for palavra in texto:
        frequencia_palavra = freq_individual(palavra,texto)
        frequencia.append((frequencia_palavra, palavra))
    return frequencia


def freq_individual(palavra,texto):
    contagem = 0
    for outras in texto:
        if outras == palavra:
            contagem += 1
    return contagem











def main():
    arquivo, stop_words = ler_entrada()
    texto = ler_arquivo(arquivo)
    texto_filtrado = filtrar_texto(texto, stop_words)
    frequencia = contar_frequencia(texto_filtrado)
