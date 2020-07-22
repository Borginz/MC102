 import argparse
def obter_argumentos():
    parser = argparse.ArgumentParser()
    '''Adicionar os argumentos que serão usados '''
    parser.add_argument('a', help = "argumento para executar o arquivo",default='agenda.csv')
    parser.add_argument('operacao', help = "operacoes que queremos realizar na agenda")
    parser.add_argument('--evento', help = 'mostra qual o evento',type=int)
    parser.add_argument('--nome', help = 'mostra o nome do evento')
    parser.add_argument('--descricao', help='descricao do evento')
    parser.add_argument('--data', help='data do evento')
    parser.add_argument('--hora', help= 'hora do evento')




def main():
    argumentos = obter_argumentos()




