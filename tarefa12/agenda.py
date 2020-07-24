import argparse


def inicializar_agenda(nome_arquivo):
    ''' Função para iniciar uma nova agenda'''
    with open(nome_arquivo, 'w') as arquivo:
        print(f'Uma agenda vazia "{nome_arquivo}" foi criada!')

def escrever_arquivo(agenda, nome_arquivo):
    '''' Função para receber o arquivo com a agenda e escrever nessa'''
    with open(nome_arquivo,'w',encoding='utf-8') as arquivo:
        for evento in agenda:
            i = evento
            nome = agenda[evento][0]
            descricao = agenda[evento][1]
            data = agenda[evento][2]
            hora = agenda[evento][3]
            arquivo.write(str(i)+','+nome+','+descricao+','+data+','+hora+'\n')

            
def ler_arquivo(agenda_csv):
    '''Função para ler o arquivo csv e devolver a agenda'''
    agenda = dict()
    with open(agenda_csv) as arquivo:
        for linhas in arquivo:
            linha = linhas.strip().split(',')
            id_evento = linha[0]
            evento = linha[1:]
            agenda[int(id_evento)] = evento
            # for idx in range(len(linha)):
    return agenda


def listar_agenda(agenda, data):
    '''Função para devolver os eventos do dia no formato csv'''
    eventos = []
    for key in agenda:  # <- esse
        if agenda[key][2] == data:
            eventos.append([key] + agenda[key])
    if len(eventos) != 0:
        print(f"Eventos do dia {data}\n" + 47 * "-")
        for evento in eventos:
            print(f"Evento {evento[0]} - {evento[1]}")
            print(f"Descrição: {evento[2].strip()}")
            print(f"Data: {evento[3]}")
            print(f"Hora: {evento[4]}")
            print(47 * "-")
    else:
        print(f"Não existem eventos para o dia {data}!")

def alterar(agenda, evento, nome, descricao, data, hora):
    '''Função para alterar a agenda dado o evento mencionado com o argumento pedido'''
    lista_alteracoes = agenda[evento]
    if nome != None:
        lista_alteracoes[0] = nome
    if descricao != None:
        lista_alteracoes[1] = descricao
    if data != None:
        lista_alteracoes[2] = data
    if hora != None:
        lista_alteracoes[3] = hora
    return agenda

    # lista_pra_alterar = dicionario[evento]
    # igualando as listas
    # lista_pra_alterar[0] = novo_nome


def criar_evento(agenda, nome, descricao, data, hora):
    '''Função para criar o evento com suas descriçoes'''


    if len(agenda) == 0:
        agenda[1] = [nome, descricao, data, hora]

    else:
        x = max(agenda)
        agenda[x + 1] = [nome, descricao, data, hora]
    return agenda


def remover_evento(agenda, evento):
    '''Função para remover o evento pedido'''
    agenda.pop(evento)
    return agenda


def receber_argumentos():
    parser = argparse.ArgumentParser()
    '''Adicionar os argumentos que serão usados '''
    parser.add_argument('-a', '--agenda', help="argumento para executar o arquivo",
    required = True)
    parser.add_argument('operacao', help="operacoes que queremos realizar na agenda")
    parser.add_argument('--evento', help='mostra qual o evento', type=int)
    parser.add_argument('--nome', help='mostra o nome do evento')
    parser.add_argument('--descricao', help='descricao do evento')
    parser.add_argument('--data', help='data do evento')
    parser.add_argument('--hora', help='hora do evento')
    args = parser.parse_args()
    return args


def main():
    args = receber_argumentos()
    evento, nome, descricao, data, hora = args.evento, args.nome, args.descricao, args.data, args.hora
    if args.operacao == 'inicializar':
        inicializar_agenda(args.agenda)
    else:
        agenda = ler_arquivo(args.agenda)
        if args.operacao == 'criar':
            agenda = criar_evento(agenda, nome, descricao, data, hora)
            escrever_arquivo(agenda, args.agenda)
        elif args.operacao == 'alterar':
            agenda = alterar(agenda, evento, nome, descricao, data, hora)
            escrever_arquivo(agenda, args.agenda)
        elif args.operacao == 'remover':
            agenda = remover_evento(agenda, evento)
            escrever_arquivo(agenda, args.agenda)
        elif args.operacao == 'listar':
            listar_agenda(agenda, data)



main()
