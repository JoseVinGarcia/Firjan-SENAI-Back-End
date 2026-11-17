public class Aluno{
    
   private String nome;
   private int idade;
   private String curso;
    
    public Aluno(String nome, int idade, String curso) {
        
        this.nome = nome;
        this.idade = idade;
        this.curso = curso;
    }
    
    public String getNome(){///Como se fosse o um funcinário que permite saber a outras classes que existe um atributo chamado nome na classe Aluno, no entando ela não deixar fazer aluteções só informa que sim, exite esse atributoo
        return nome;
    }
    
    public void setNome(String novoNome){
        this.nome = novoNome;
    }
    
    public int getIdade(){
        
        return idade;
    }
    
    public String getCurso(){
        return curso;
    }
    
    
}