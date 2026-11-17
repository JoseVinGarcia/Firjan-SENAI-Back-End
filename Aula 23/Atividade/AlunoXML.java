import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

// essa classe, diferente da aluno para registrar dados, é a classe para registrar os arquivos
public class AlunoXML {
    public static void salvar(ArrayList<Aluno> alunos) {
        try {
            FileWriter writer = new FileWriter("aluno.xml");
            
            // cria a tag principal do xml
            writer.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
            writer.write("<alunos>\n");
            
            // percorre todos os alunos cadastrados
            for (Aluno aluno : alunos) {
                writer.write("  <aluno>\n");
                writer.write("  <nome>" + aluno.getNome() + "</nome>\n");
                writer.write("  <idade>" + aluno.getIdade() + "</idade>\n");
                writer.write("  <curso>" + aluno.getCurso() + "</curso>\n");
                writer.write("  <aluno>\n");
            }
            
            // fecha a tag principal
            writer.write("</alunos>");
            writer.close();
            System.out.println("XML gravado!");
        } catch (Exception e) {
            System.out.println("XML não conseguiu ser gravado: " + e.getMessage());
        }
    }
    
    // Método para mostrar o conteudo do XML
    public static void mostrarXML(){
        try {
            BufferedReader reader =
                new BufferedReader(
                new FileReader("aluno.xml"));
                
            String linha;
            
            System.out.println("\n=== CONTEÚDO DO XML ===");
            
            while ((linha = reader.readLine()) != null) {
                System.out.println(linha);
            }
            
            reader.close();
            
        } catch (Exception e) {
            System.out.println("XML não conseguiu ser lido: " + e.getMessage());
        }
    }
}
