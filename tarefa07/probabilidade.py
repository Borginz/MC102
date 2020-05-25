"""
Tendo uma lista ( L ), faça a contagem das frequencias que nela aparece, elimine a repetição da lista original e ordene numa segunda lista

"""
L = input().split()
L2= []
n = 0

for i in L:
    i=int(i)
    if i > n:
        n=i
F = [0]*(len(L)+1)
for i in L:
    i = int(i)
    F[i] += 1
F2 = []
for i in F:
    if i != 0:
        F2.append(i)
for i in L:
    if i not in L2:
        L2.append(i)
for i in range(len(L2)-1):
    for i in range(len(L2)-1):
        if L2[i]> L2[i+1]:
            aux = L2[i]
            L2[i]= L2[i+1]
            L2[i+1]= aux
for i in range(len(F2)-1):
    for i in range(len(F2)-1):
        if F2[i]>F2[i+1]:
            aux = F2[i]
            F2[i] = F2[i + 1]
            F2[i + 1] = aux
            aux2 = L2[i]
            L2[i] = L2[i + 1]
            L2[i + 1] = aux
for i in L2:
    print(i, end=' ')
