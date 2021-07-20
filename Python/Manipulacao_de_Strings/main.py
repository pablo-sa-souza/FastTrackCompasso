url = "bytebank.com/cambio?moedaDestino=Dolar&moedaOrigem=real" #Url original

url = "     "  #URL para teste

#Sanitização
#url = url.replace(" ", "") #Solução para substituir valores
url = url.strip() #Solução para limpar espaços (existe o lstrip (tira a esquerda) e o rstrip(tira a direita))

#Validação URL
if url == "":
    raise ValueError ("url está vazia")

#separa base dos parametros
indice_interrogacao = url.find("?") #Define a ? como divisor da URL e dos parametros.
url_base = url[0:indice_interrogacao] # da interrogação para tras temos a base da URL.
url_parametros = url[indice_interrogacao+1:] #define os parametros como sendo o que está a direita do indice.

parametro_busca= 'moedaDestino' #Especifica o parametro a ser buscado.
indice_parametro = url_parametros.find(parametro_busca) #Define a posição do parametro.
indice_valor = indice_parametro + len(parametro_busca)+1 #Define o indice do valor sendo o indice do parametro + o tamanho do parametro_busca +1 (referente ao sinal de =)
indice_e_comercial = url_parametros.find('&', indice_valor) #find (parametro, a partir de)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:] #mostra o valor.
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(url_parametros)
print(valor)