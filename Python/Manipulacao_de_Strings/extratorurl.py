import re #importação do modulo regex

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        self.get_url_base()
        self.get_url_parametros()
        self.converte()

    def sanitiza_url(self, url):
        if type(url) == str:    #valida se a URL tem string
            return url.strip()  #limpa url
        else:
            return ""
    
    def valida_url(self):
        if not self.url:
            raise ValueError("a url esta vazia")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError ("a url não é valida")
        else:
            print("é valida")
    
    def get_url_base(self):
        indice_interrogacao = self.url.find("?") #Define a ? como divisor da URL e dos parametros.
        url_base = self.url[:indice_interrogacao] # da interrogação para tras temos a base da URL.
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?") #Define a ? como divisor da URL e dos parametros.
        url_parametros = self.url[indice_interrogacao+1:] #define os parametros como sendo o que está a direita do indice
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca) #Define a posição do parametro.
        indice_valor = indice_parametro + len(parametro_busca)+1 #Define o indice do valor sendo o indice do parametro + o tamanho do parametro_busca +1 (referente ao sinal de =)
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor) #find (parametro, a partir de)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:] #mostra o valor.
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def __len__(self):
        return len(self.url)

    def __str__ (self):
        return self.url + "\n" + " Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def converte(self):
        moeda_origem = self.get_valor_parametro("Origem")
        moeda_destino = self.get_valor_parametro("Destino")
        valor_quantidade = float(self.get_valor_parametro("quantidade"))
        valor_dolar = 5.50 
        
        if moeda_origem == "dolar" and moeda_destino == "real":
            valor_convertido = valor_quantidade * valor_dolar
            return print(f"valor convertido é:{valor_convertido}")
        else:
            print ("valores invalidos")


extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real")


