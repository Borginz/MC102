from modulo import*

def mostrar_arvore(url_inicio,url_atual,nivel,lista_printados):
    '''Função para imprimir a arvore de links mostrando a hierarquia a partir do inicial. Começa
    obtendo uma string com o conteudo do html, procurando pelo padrao com o  regex armazenando na
    lista_html,percorrendo as url's e analisando pela função resolver_url(analisar url's incompletas),
    se a url nao estiver sido printada anteoriormente e for validada pela função "eh_url_valida" ela
    é printada com os devidos espaços e é chamada a recursao" '''


    html_atual = obter_html(url_atual)
    regex = r'href="(.*?)"'
    lista_html = re.findall(regex,html_atual)
    for url in lista_html:
        url = resolver_url(url,url_atual)
        if url not in lista_printados and eh_url_valida(url,url_inicio):
            lista_printados.append(url)
            print(' '*nivel*2+url)
            mostrar_arvore(url_inicio,url,nivel+1,lista_printados)


def main():
    url_inicio = input()
    lista_printados = []
    url_atual = url_inicio
    mostrar_arvore(url_inicio,url_atual,0,lista_printados)
main()