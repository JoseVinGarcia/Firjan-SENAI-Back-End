# AULA 05 - Dicionário
from funcoes import cadastrar_livros, listar_livros

livro = []

while True:
    print("\n>>> BIBLIOTECA <<<")
    print("1 - CADASTRO")
    print("2 - LISTAR")
    print("3 - SAIR")

    op = input("Escolha uma opção: ")

    if op == "1":
        cadastrar_livros(livro)
    elif op == "2":
        listar_livros(livro)
    elif op == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida")
