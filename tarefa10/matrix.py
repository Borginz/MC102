imagem = []
imagem.append([" "]*8)
for i in range(5):
    if i < 6:
        imagem.append(imagem[0])
print(len(imagem))
print (imagem)