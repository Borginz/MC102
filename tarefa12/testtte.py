agenda = dict()
nome = "mc102"
descricao = "plipli"
data = "04/08"
hora = "14:00"
agenda[1] = [nome,descricao,data,hora]

for evento in agenda:
    i = evento
    nome = agenda[evento][0]
    descricao = agenda[evento][1]
    data = agenda[evento][2]
    hora = agenda[evento][3]

    print(nome)