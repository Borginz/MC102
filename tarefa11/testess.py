def remover_pontuacao(palavra):
    pontuacao = ",.;:?!''"
    palavra_certa = ""
    for letra in palavra:
        if letra not in pontuacao:
            palavra_certa += letra
    return palavra_certa
def contar_frequencia(texto):
    freq = dict()
    for chave in texto:
        if chave not in freq:
            freq[chave] = 1
        else:
            freq[chave] += 1
    return freq
def filtrar_texto(texto):
    texto_filtrado = []
    for palavras in texto:
        palavra_certa = remover_pontuacao(palavras)
        texto_filtrado.append(palavra_certa)
    return texto_filtrado




def main():
    texto = ['caramba.','cachorro?','coelho','coelho','cachorro.','alce']
    texto_filtrado = filtrar_texto(texto)
    frequencia = contar_frequencia(texto_filtrado)
    print(frequencia)




main()