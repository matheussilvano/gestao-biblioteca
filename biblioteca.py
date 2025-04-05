from autor import Autor
from capitulo import Capitulo
from editora import Editora
from livro import Livro

class Biblioteca:

    def __init__(self, livro: Livro = None):
        self.livros = []
        if livro is not None:
            self.livros.append(livro)


    def incluir_livro(self, livro: Livro):
        if not isinstance(livro, Livro):
            print("Este objeto não é um Livro!")

        elif livro not in self.livros:
            self.livros.append(livro)
        else:
            print(f'O livro {livro.titulo} já foi adicionado.')
            return None
        
    def excluir_livro(self, livro: Livro):
        if livro in self.livros:
            self.livros.remove(livro)
        else:
            print(f'O livro {livro.titulo} não existe na biblioteca.')
            return None
        
    def buscar_livro_por_titulo(self, titulo):
        for livro in self.livros: 
            if livro.titulo == titulo:
                return livro
        return None

    def listar_livros(self):
        return self.livros 



if __name__ == "__main__":
    from autor import Autor
    from capitulo import Capitulo
    from editora import Editora
    from livro import Livro

    print("\n===== TESTE FUNCIONAL DA BIBLIOTECA =====")

    # Criando autores e editora
    autor1 = Autor(1, "João Silva")
    autor2 = Autor(2, "Maria Souza")
    editora1 = Editora(1, "Editora Saber")

    # Criando livros
    livro1 = Livro(101, "Python para Iniciantes", 2022, editora1, autor1)
    livro1.incluir_capitulo(1, "Introdução")
    livro1.incluir_capitulo(2, "Tipos de Dados")

    livro2 = Livro(102, "Dominando Python", 2023, editora1, autor2)
    livro2.incluir_capitulo(1, "Funções")
    livro2.incluir_capitulo(2, "Orientação a Objetos")

    # Criando biblioteca
    biblioteca = Biblioteca()

    print("\n📚 Adicionando livros na biblioteca:")
    biblioteca.incluir_livro(livro1)
    biblioteca.incluir_livro(livro2)

    print("\n📋 Listando livros:")
    for l in biblioteca.listar_livros():
        print(f"📘 {l.codigo} - {l.titulo} ({l.ano})")
        print("   📄 Capítulos:")
        for capitulo in l.capitulos:
            print(f"     ➤ Capítulo {capitulo.numero}: {capitulo.titulo}")

    print("\n🔍 Buscando livro por título 'Dominando Python':")
    buscado = biblioteca.buscar_livro_por_titulo("Dominando Python")
    if buscado:
        print(f"✅ Encontrado: {buscado.titulo}")
    else:
        print("❌ Livro não encontrado.")

    print("\n🧪 Teste: Tentando adicionar objeto que não é livro:")
    class FalsoLivro:
        pass
    obj_estranho = FalsoLivro()
    biblioteca.incluir_livro(obj_estranho)  # Deve ser ignorado

    print("\n🗑️ Removendo livro 'Python para Iniciantes':")
    biblioteca.excluir_livro(livro1)

    print("\n📋 Lista final de livros:")
    for l in biblioteca.listar_livros():
        print(f"📘 {l.codigo} - {l.titulo}")
        print("   📄 Capítulos:")
        for capitulo in l.capitulos:
            print(f"     ➤ Capítulo {capitulo.numero}: {capitulo.titulo}")


    print("\n✅ Teste finalizado com sucesso.")



