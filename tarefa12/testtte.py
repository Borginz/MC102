agenda = dict()
nome = "MC102"
descricao = "Aula de laboratorio"
data = "01/06/2020"
hora = "14:00"
agenda[1] =[nome,descricao,data,hora]
x = max(agenda)
agenda[x+1] = [nome,descricao,data,hora]
print(agenda)
for evento in agenda:
    print(nome)