Algoritmo para identificar o numero com maior numero de divisores

  O computador deverá ser capaz de :
- Efutuar as 4 operações matemáticas básicas
- Anotar um número ou mais
- Fazer uma leitura se uma divisão é exata ou não
- Identificar o número anotado
- Contar números

                        ENTRADAS:
Tem-se a entrada como um conjunto de n números inteiros positivos.
                         SAÍDA:
A saída é algum número da entrada que contiver o maior número de divisores.
Se houver vários números com essa mesma quantidade de divisores, então a saída pode ser qualquer um deles.


Definição de números primos:

- Para um número ser primo ele:
- Não deve ser divisível por 2 exceto o próprio 2
- Não deve ser divisível por 3,5 ou 7
- deve ter apenas dois divisores positivos 

Repita esse processo n-1 vezes
Dada as entradas de n números deverá fazer a checagem dos divisores de cada n número dessa forma:
- Divida o número pelo menor primo possível sucessivamente até aquele se tornar em valor 1;
- Anote todos os números primos usados;
- Conte quantas vezes cada primo apareceu separadamente;
- Anote a quantidade de cada;
- Some 1 a cada quantidade de primos usados;
- Anote os novos números;
- Multiplique os novos números para obter o número de divisores dele;
- Anote o número obtido separadamente;

Compare os números obtidos e identifique o maior entre eles;
- identifique de qual n número aquele valor foi obtido
- De como saída esse n número identificado
- Caso dois n números tenham o mesmo número de divisores dê os dois como saída





