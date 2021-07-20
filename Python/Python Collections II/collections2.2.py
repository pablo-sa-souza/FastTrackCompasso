from collections import defaultdict
from collections import Counter

texto = "Agora que já sabemos utilizar conjuntos e dicionários, eu quero fazer um trabalho que estávamos fazendo agora a pouco: estávamos tentando pegar um texto, um texto que eu tinha aqui em cima, vou pegar esse texto específico. E o que eu quero fazer é realmente contar o número de aparições de cada palavra dentro desse texto. Então o meu primeiro passo vai ser resolvermos essa questão do maiúsculo ou minúsculo. Então eu vou querer transformar essa string em minúscula."

texto = texto.upper()
'''aparicoes = {}

for palavra in texto.split(): 
    por_enquanto = aparicoes.get(palavra, 0)   #esse trecho retorna uma conagem de palavras no texto.
    aparicoes[palavra] = por_enquanto + 1

print(aparicoes)'''

#aparicoes = defaultdict(int)

'''for palavra in texto.split(): 
       #esse trecho retorna uma conagem de palavras no texto como acima mas usando default dict
    aparicoes[palavra] += 1

print(aparicoes)'''

aparicoes =  Counter(texto.split())

print(aparicoes)