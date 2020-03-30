Algoritmo para somar dias a uma data

Instruções elementares necessárias para a soma:
Será necessário a capacidade da máquina de:
- Realizar as 4 operações básicas da matemática
- Anotar um número ou mais
- Fazer uma leitura se uma divisão é exata ou não
- Identificar o número anotado

Condições para as entradas e saídas:

Tem-se definido que a variável "mes" pertence ao intervalo [1,12]
Para os meses (1,3,5,7,8,10,12):
Tem-se definido que a variável "dia" pertence ao intervalo [1,31]
Para os meses (4,6,9,11):

Tem-se definido que a variável "dia" pertence ao intervalo [1,30]
Para o mês (2):
Tem-se definido que a variável "dia":
Se o ano for bissexto pertence ao intervalo [1,29]
Se o ano não for bissexto pertence ao intervalo [1,28]

Tem-se definido que a variável "ano" pertence ao intervalo [0,8000]
Se a variável "ano" for divisível por 4 , então é bissexto
Se a variável "ano" for divisível por 400, então é bissexto
Se a variável "ano" não for divisível por 4, então não é bissexto
Se a variável "ano" for divisível por 4 e 100 e não por 400, então não é bissexto

Anote dia/mes/ano
Anote o número da variável soma

Faça uma adição da variável dia com soma:
Se a adição estiver dentro do intervalo de "dia"
Anote o novo valor de dia
Se a adição "dia" + "soma" for maior que o ultimo valor estipulado no intervalo para "dia":
Deve se fazer "soma" - "dia", adicionar 1 na variável "mes" e o valor da subtração em "dia";
Anote o novo valor de dia e mes
Se a adição "dia" + "soma" for maior que o ultimo valor estipulado para dia e "mes" tiver valor 12:
Adicione 1 na variável "ano", tome como novo valor 1 para "mes" e o valor da subtração "soma" - "dia" para "dia"
Anote o novo valor de dia, mes e ano


dê como saída a nova data dia/mes/ano















