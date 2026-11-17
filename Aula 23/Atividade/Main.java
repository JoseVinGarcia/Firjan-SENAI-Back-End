import java.util.Scanner;
import java.util.ArrayList;

public class Main
{
	public static void main(String[] args) {
	    Scanner leitura = new Scanner(System.in);
	    
	    ArrayList<Aluno> alunos = new ArrayList<>();
	    
	    String resposta;
	    
		do {
		    // Pede e insere os dados
		    System.out.println("Digite o nome do aluno:");
		    String nome = leitura.nextLine();
		    
		    System.out.println("Digite a idade do aluno:");
		    int idade = leitura.nextInt();
		    
		    leitura.nextLine();
		    
		    System.out.println("Digite o curso do aluno:");
		    String curso = leitura.nextLine();
		    
		    // Registrando
		    Aluno aluno = new Aluno(nome,idade,curso);
		    alunos.add(aluno);
		    
		    System.out.println("Deseja cadastrar outro aluno? S/N:");
		    resposta = leitura.nextLine();
		    
		} while (resposta.equalsIgnoreCase("S")); // Caso seja S maiusculo
		    
		    System.out.println("Cadastro encerrado!");
		    
		    AlunoXML.salvar(alunos);
		    
		    AlunoXML.mostrarXML();
		    
		    leitura.close();
	}
}
