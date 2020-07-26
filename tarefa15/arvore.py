from modulo import*

def obter_html(url):

    nome_cache = obter_nome_cache(url)

    if os.path.isfile(nome_cache):
        with open(nome_cache, encoding="UTF-8") as arquivo:
            html = arquivo.read()
    else:
        if not REQUESTS_FOUND:
            print("O módulo requests é necessário para baixar outras páginas:", file=sys.stderr)
            print("tente digitar:  pip3 install --user requests", file=sys.stderr)
            sys.exit(1)
        response = requests.get(url, allow_redirects=True)
        if response.status_code != 200:
            return None
        try:
            html = response.content.decode("UTF-8")
        except UnicodeDecodeError:
            html = response.content.decode("ISO-8859-1")
        if "text/html" not in response.headers["Content-Type"]:
            return None
        with open(nome_cache, "w", encoding="UTF-8") as arquivo:
            arquivo.write(html)

    return html


def mostrar_arvore(url_inicio,url_atual,espacos,lista_printados):
    '''Função para imprimir a arvore de links mostrando a hierarquia a partir do inicial,
    obtendo uma string com o conteudo do html, procurando pelo padrao com o  regex armazenando na
    lista_html,percorrendo as url's e analisando pela função resolver_url(analisar url's incompletas),
    se a url nao estiver sido printada anteoriormente e for validada pela função "eh_url_valida" ela
    é printada comos devidos espaços e é chamada a recursao" '''


    html_atual = obter_html(url_atual)
    regex = r'href="(.*?)"'
    lista_html = re.findall(regex,html_atual)
    for url in lista_html:
        url = resolver_url(url,url_atual)
        if url not in lista_printados and eh_url_valida(url,url_inicio):
            lista_printados.append(url)
            print(' '*espacos*2+url)
            mostrar_arvore(url_inicio,url,espacos+1,lista_printados)


def main():
    url_inicio = input()
    lista_printados = []
    url_atual = url_inicio
    mostrar_arvore(url_inicio,url_atual,0,lista_printados)
main()