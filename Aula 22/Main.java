// AULA 22 - JAVA
// Todo codigo tem um arquivo Main

public class Main
{
	public static void main(String[] args) {
		// Criamos um cachorro chamado Rex, da classe Cachorro
	    Cachorro c = new Cachorro("Rex");
		System.out.println("Meu cachorro se chama "+c.nome);
		System.out.println("E no momento ele está "+c.dormir());
		
		// E um boi chamado Pé de pano, da classe Boi
		Boi b = new Boi("Pé de Pano");
		System.out.println("Eu tenho um boi e ele se chama "+b.nome);
		System.out.println("Mas agora ele está "+b.dormir());
		
		
	}
}
