class Calc:

    def __init__ (self, nm1, nm2, op):
        self.nm1 = nm1
        self.nm2 = nm2
        self.op = op
       

    def calculadora(self):
        if(self.op == "+"):
            print(self.nm1 + self.nm2)
        elif(self.op == "-"):
            print(self.nm1 - self.nm2)
        elif(self.op == "*"):
            print(self.nm1 * self.nm2)
        elif(self.op == "/"):
            print(self.nm1 / self.nm2)
            

teste = Calc(10,15, "/")

teste.calculadora()
