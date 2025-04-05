class Autor:
    
    def __init__(self, codigo: int, nome: str):
        self.__codigo = codigo
        self.__nome = nome
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo
    
    @codigo.getter
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @nome.getter
    def nome(self):
        return self.__nome