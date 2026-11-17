# Aula 10
# Sistema: Biblioteca

# Criando o banco de dados
CREATE DATABASE Biblioteca;

# Criando a tabela Autores
CREATE TABLE Autores(
	id_autor INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(100) NOT NULL,
	nacionalidade VARCHAR(50)
);

# Criando a tabela livros
CREATE TABLE Livros(
	id_livro INT PRIMARY KEY AUTO_INCREMENT,
	titulo VARCHAR(150) NOT NULL,
	ano_publicacao INT,
	FOREIGN KEY (id_autor) REFERENCES Autores(id_autor) 
);

# Adicionando uma coluna em livros
ALTER TABLE Livros 
ADD categoria VARCHAR(50);

# Alterando o titulo para Varchar(200)
ALTER TABLE Livros
MODIFY titulo VARCHAR(200) NOT NULL;

# Criando a tabela usuarios
CREATE TABLE Usuarios(
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(150) NOT NULL,
	email VARCHAR(150) NOT NULL UNIQUE 
);

# Renomeando tablea Usuarios
ALTER TABLE Usuarios
RENAME TO Leitores;

# Removendo coluna da tabela
ALTER TABLE Livros DROP COLUMN categoria;

# Apagando tabela
DROP TABLE Leitores;

# Apagando o Banco de Dados
DROP DATABASE Biblioteca;
