 import argparse
def obter_argumentos():
    parser = argparse.ArgumentParser()
    '''Adicionar os argumentos que serão usados '''
    parser.add_argument('-a',help = "argumento para executar o arquivo", required=True)
    parser.add_argument('operacao', help = "operacoes que queremos realizar na agenda")
    parser.add_argument('--evento', help = 'mostra qual o evento',type=int)
    parser.add_argument('--nome', help = 'mostra o nome do evento')
    parser.add_argument('--descricao', help='descricao do evento')
    parser.add_argument('--data', help='data do evento')
    parser.add_argument('--hora', help= 'hora do evento')

    args = parser.parse_args()
    return args

def executar_acao(args):
    agenda = args.a
    operacao = args.operacao
    evento = args.evento
    nome = args.nome
    descricao = args.descricao
    data = args.data
    hora = args.hora

    if operacao == "inicializar":
        iniciar_agenda(agenda)

    if operacao == "criar":
        pass

    if operacao == "alterar":
        pass

    if operacao == "listar":
        pass

    if operacao == "remover":
        pass

def iniciar_agenda(agenda):
    


def main():
    argumentos = obter_argumentos()
    executar_acao(argumentos)




