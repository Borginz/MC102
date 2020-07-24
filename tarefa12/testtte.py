def ler_arquivo(agenda_csv):
    agenda = dict()
    with open(agenda_csv) as arquivo:
        for linhas in arquivo:
            linha = linhas.strip().split(',')
            id_evento = linha[0]
            evento = linha[1:]
            agenda[int(id_evento)] = evento
        return agenda