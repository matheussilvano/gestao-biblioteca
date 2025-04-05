class Capitulo:
    
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo = titulo
    
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero
    
    @numero.getter
    def numero(self):
        return self.__numero

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @titulo.getter
    def titulo(self):
        return self.__titulo
    

    