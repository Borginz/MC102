def ler_entrada():
    arquivo = input
    lista_pares = []
    while True:
        try:
            par = input()
            lista_pares.append(par)
        except EOFError:
            break
    return arquivo, lista_pares

def ler_arquivo(nome_do_arquivo):
    texto = []
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavras = linha.strip().split()
            for idx in range(len(palavras)):
                texto.append(palavras[idx])
    return texto


def obter_freq(texto,pares):
    dict_freq = dict()
    par = pares.split()
    for k in range(len(texto)-2):
        if par[0]==texto[k] and par[1]==texto[k+1]:
            if texto[k+2] not in dict_freq:
                dict_freq[texto[k+2]] = 1
            else:
                dict_freq[texto[k+2]]+= 1
    return dict_freq
def remover_pontuacao(palavra):
    pontuacao = ",.;:?!''"
    palavra_certa = ""
    for letras in palavra:
        if letras not in pontuacao:
            palavra_certa += letras
    return palavra_certa


def filtrar_texto(texto):
    texto_filtrado = []
    for palavras in texto:
        palavras = palavras.lower()
        palavra_certa = remover_pontuacao(palavras)
        texto_filtrado.append(palavra_certa)
    return texto_filtrado


def obter_maior(dict):
    tuplas = []
    lista_maiores = []
    for k, v in dict.items():
        tuplas.append((k, v))
    tuplas.sort(key=lambda x: x[1])
    maior = tuplas[0][1]
    for elemento in tuplas:
        if elemento[1] == maior:
            lista_maiores.append(elemento[0])
    lista_maiores.sort()
    return lista_maiores[0]





def gerar_saida(pares,texto_filtrado):
    for par in pares:
        dict_freq = obter_freq(par,texto_filtrado)
        frequente = obter_maior(dict_freq)
        print(par,frequente)







def main():
    nome_arquivo, lista_pares = ler_entrada()
    texto = ler_arquivo(nome_arquivo)
    texto_filtrado = filtrar_texto(texto)
    gerar_saida(lista_pares,texto_filtrado)


main()