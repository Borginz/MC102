 import argparse
def obter_argumentos():
    parser = argparse.ArgumentParser()
    '''Adicionar os argumentos que serão usados '''
    parser.add_argument('-a','--agenda'help = "argumento para executar o arquivo", required=True)
    parser.add_argument('operacao', help = "operacoes que queremos realizar na agenda")
    parser.add_argument('--evento', help = 'mostra qual o evento',type=int)
    parser.add_argument('--nome', help = 'mostra o nome do evento')
    parser.add_argument('--descricao', help='descricao do evento')
    parser.add_argument('--data', help='data do evento')
    parser.add_argument('--hora', help= 'hora do evento')

    args = parser.parse_args()
    return args

'''def executar_acao(args):
    agenda = args.agenda
    operacao = args.operacao
    evento = args.evento
    nome = args.nome
    descricao = args.descricao
    data = args.data
    hora = args.hora
    anotacoes_agenda = dict()'''


def inicializar_agenda(nome_arquivo):
    with open(nome_arquivo,'w') as arquivo:
        arquivo.write(dict())
    print('Uma agenda vazia "agenda.csv" foi criada!')
    return

def ler_arquivo(agenda_csv):
    with open(agenda_csv) as arquivo:
        agenda = arquivo.readlines()
        agenda = eval(agenda)
    return agenda

def alterar(evento,nome,descricao,data,hora,agenda):





def criar_agenda(nome,descricao,data,hora,agenda):







def main():
     parser = argparse.ArgumentParser()
     '''Adicionar os argumentos que serão usados '''
     parser.add_argument('-a', '--agenda', help = "argumento para executar o arquivo", required = True)
     parser.add_argument('operacao', help="operacoes que queremos realizar na agenda")
     parser.add_argument('--evento', help='mostra qual o evento', type=int)
     parser.add_argument('--nome', help='mostra o nome do evento')
     parser.add_argument('--descricao', help='descricao do evento')
     parser.add_argument('--data', help='data do evento')
     parser.add_argument('--hora', help='hora do evento')
     args = parser.parse_args()
     if args.operacao == 'inicializar':
         inicializar_agenda(args.agenda)
     else:
         agenda = ler_arquivo(args.agenda)
         if args.operacao == 'criar':
             criar_agenda(agenda)
         elif args.operacao == 'alterar':
              alterar_agenda(agenda)
         elif args.operacao == 'remover':
              remover_agenda(agenda)
         elif args.operacao == 'listar':
             listar_agenda(agenda)









