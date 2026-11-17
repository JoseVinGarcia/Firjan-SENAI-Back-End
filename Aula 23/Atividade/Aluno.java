public class Aluno {
    private String nome;
    private int idade;
    private String curso;
    
    // Criando a class aluno
    public Aluno(String nome, int idade, String curso) {
        this.nome = nome;
        this.idade = idade;
        this.curso = curso;
    }
    
    // criando os metodos
    public String getNome() {
        return nome;
    }
    
    public void setNome(String novoNome) {
        this.nome = novoNome;
    }
    
    public int getIdade() {
        return idade;
    }
    
    public String getCurso() {
        return curso;
    }
}
