# AULA 05 - Funcoes
def cadastrar_livros(livros):

    while True:
        livro = {}

        # Nos registros, ao inves do indice, salvamos com um "nome"
        livro["título"] = input("Título: ") # O Titulo como se fosse uma variavel 'titulo' dentro de Livro
        livro["autor"] = input("Autor: ")
        livro["ano"] = input("Ano de Lançamento: ")

        livros.append(livro)

        op = input("Deseja continuar com o cadastro? (S/N):")

        if op.upper() != "S":
            break

def listar_livros(livros):
    if len(livros) == 0:
        print("Não existem livros cadastrados")
        return

    print("\n>>> LISTA DE LIVROS <<<")

    for livro in livros:
        print("Título: ",livro["título"])
        print("Autor: ",livro["autor"])
        print("Ano de Lançamento: ",livro["ano"])
        print("_" * 20)
