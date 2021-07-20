class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("saldo {} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self,valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_sacar = self.__saldo+self.limite
        return valor_a_sacar <= valor_disponivel_sacar
    
    def saca(self, valor):
        if(self.__pode_sacar):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
        
    def transfe(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    @property
    def saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property #property fica atrelado ao objeto
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite): 
        self.__limite = limite
    
    @staticmethod #staticmethod esta atrelado a classe
    def codigo_banco(self):
        return "001"

 #codigo abaixo para ser executado no console
'''
python
from conta import Conta
#criando os objetos
conta = Conta(123, "Nico", 55.5, 1000.0)
conta2 = Conta(321, "Marco", 100.0, 1000.0)
#testando transferencia
conta2.transfere(10, conta)
 '''