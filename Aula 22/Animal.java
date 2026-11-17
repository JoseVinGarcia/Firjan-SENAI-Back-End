// Superclasse (Classe pai) animal
// O abstract quer dizer que essa classe nao pode ser replicada diretamente
public abstract class Animal {
    
    // Recebe um valor só, nome
    String nome;
    
    public Animal(String nome) {
        
        this.nome = nome;
    }
    
    // Ela tem tambem esse metodo fazerSom, que a principio nao recebe parametro, pois cada animal faz um som de forma diferente.
    // O void quer dizer que ela não da return
    public abstract void fazerSom();
}