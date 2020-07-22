dict = {"gato":1,"cachorro":1,"aviao":2,"avestruz":1,"onça":3}
tuplas = []
for k, v in dict.items():
    tuplas.append((k, v))
tuplas.sort(key=lambda x: x[0])
print(tuplas)
tuplas.sort(key=lambda x:x[1], reverse=True)
print(tuplas)


