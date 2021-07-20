idades = [15, 20, 50, 8, 95, 45, 4]

#print (list(enumerate(idades))) #dessa forma traz posição+idades

#print (list(range(len(idades)))) #aqui tras somente as posições.

'''for valor in enumerate(idades): #aqui tras posição+idades em lista
    print(valor)'''

#print (sorted(idades)) #ordena os elementos em ordem crescente

#print(list(reversed(idades))) #apresenta os valores na ordem invertida da inserção

print (sorted(idades), reversed) #ordena os valores em ordem decrescente


usuarios = [
    ("guilherme", 37, 1981),
    ("daniela", 28, 1990),
    ("marcos", 18, 1999)
]

for nome, idade, nascimento in usuarios: #posso ignorar os elementos idade e nascimento os substituindo por _
    print(nome)