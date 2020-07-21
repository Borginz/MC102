def ler_entrada():
    arquivo = input
    lista_pares = []
    while True:
        try:
            par = input().split()
            lista_pares.append(par)
        except EOFEerror:
            break
    return arquivo, lista_pares

def ler_arquivo(nome_arquivo):
    texto = []
    with open(nome_arquivo, 'r', encoding='utf-8'):
        for linha in arquivo:
            palavras = linha.strip().split()
            for idx in range(len(palavras)):
                texto.append(palavras[idx])

def filtrar_texto(texto):
    texto_sem_stop = []
    texto_filtrado = []
    pontuacao = ['!', '!\n', '?', ' ?\n', '.\n', ',', '.', ':', '"', ';']
    for palavra in texto:
        if palavra not in stop_words:
            texto_sem_stop.append(texto_filtrado)
    for filtrada in texto_sem_stop:
        if filtrada not in texto_sem_stop:
            texto_filtrado.append(filtrada)
    return texto_filtrado
def obter_freq(texto,pares):
    dict_freq = dict()
    for k in range(len(texto)-2):
        if pares[0]==texto[k] and pares[1]==texto[k+1]:
            if texto[k+2] not in dict_freq:
                dict_freq[texto[k+2]] = 1
            else:
                dict_freq[texto[k+2]]+= 1
    return dict_freq

def obter_maximo(dict):
    maior = max(dict, key = lambda chave: len(dict[chave]))
    lista_maiores = []
    for palavra in dict.keys():
        if dict[palavra] == maior:
            lista_maiores.append(palavra)
        lista_maiores.sort()
    return lista_maiores[0]

def gerar_saida(pares,dict):
    elemento_maximo = obter_maximo(dict)
    for palavra in pares:
        print(palavra+' '+elemento_maximo)






def main():
    nome_arquivo, lista_pares = ler_entrada()
    texto = ler_arquivo(arquivo)
    texto_filtrado = filtrar_texto(texto)
    dict_freq = obter_freq(texto_filtrado,lista_pares)
    obter_maximo(lista_pares,dict_freq)
    gerar_saida(lista_pares)

main()