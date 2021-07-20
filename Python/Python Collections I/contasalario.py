class ContaSalario:

    def __init__ (self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita (self, valor):
        self._saldo += valor
    
    def __eq__(self,outro):
        if type(outro) != ContaSalario:
            return False
        return print(self._codigo == outro._codigo and self._saldo == outro._saldo) 
       
    def __str__(self):
        return "[>>Codigo {} saldo {}<<]".format(self._codigo, self._saldo)


conta1 = ContaSalario(12)


conta2 = ContaSalario(12)

print(conta1)

print(conta2)

conta1 == conta2