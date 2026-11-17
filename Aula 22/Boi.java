// Aqui diz que o Boi vem da classe Animal
public class Boi extends Animal {
    
    public Boi(String nome) {
        // o super redireciona pra superclasse Animal
        super(nome);
        
    }
    // O Override significa que ele esta sobrescrevendo um metodo da classe original
    @Override
    public void fazerSom() {
        System.out.println("Muuu!");
    }
    
    // O metodo dormir só retorna que ele esta dormindo.
    public String dormir() {
        
        return "Dormindo...";
    }
}