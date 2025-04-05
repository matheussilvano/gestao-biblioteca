from autor import Autor
from capitulo import Capitulo
from editora import Editora

class Livro: 
 
    def __init__(self, codigo: int, titulo: str, ano:int, editora: Editora, autor: Autor, numero_capitulo: int = None, titulo_capitulo: str = None):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.editora = editora
        self.autores = []

        self.incluir_autor(autor)
        
        self.__capitulos = []
        if numero_capitulo is not None and titulo_capitulo is not None:
            self.incluir_capitulo(numero_capitulo, titulo_capitulo)


    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        self.__ano  = novo_ano

    @property
    def capitulos(self):
        return self.__capitulos

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor) and autor not in self.autores:
            self.autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if autor in self.autores:
            self.autores.remove(autor)

    def incluir_capitulo(self, numero: int, titulo: str):
        # Verifica se já existe um capítulo com esse título
        if self.find_capitulo_by_titulo(titulo) is None:
            self.__capitulos.append(Capitulo(numero, titulo))
        else:
            print(f"Capítulo '{titulo}' já existe no livro '{self.titulo}'.")


    def excluir_capitulo(self, titulo: str):
        cap = self.find_capitulo_by_titulo(titulo)
        if cap:
            self.__capitulos.remove(cap)
        else:
            print(f"Capítulo '{titulo}' não encontrado.")



    def find_capitulo_by_titulo(self, titulo: str):
        for cap in self.__capitulos:
            if cap.titulo == titulo:
                return cap
        return None

