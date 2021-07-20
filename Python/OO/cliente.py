class Cliente:
    def __init__(self, nome):
        self.__nome = nome
    
    @property #atrela a função ao atributo
    def nome(self):
        return self.__nome.title()

    @nome.setter #função para alteração de nome
    def nome(self, nome):
        self.__nome = nome