
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class AlunoXML {

    // Método para salvar vários alunos no mesmo arquivo XML
    public static void salvar(ArrayList<Aluno> alunos) {

        try {

            FileWriter writer = new FileWriter("aluno.xml");

            // Cria a tag principal do XML
            writer.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n");
            writer.write("<alunos>\n");

            // Percorre todos os alunos cadastrados
            for (Aluno aluno : alunos) {

                writer.write("   <aluno>\n");

                writer.write("      <nome>"
                        + aluno.getNome() + "</nome>\n");

                writer.write("      <idade>"
                        + aluno.getIdade() + "</idade>\n");

                writer.write("      <curso>"
                        + aluno.getCurso() + "</curso>\n");

                writer.write("   </aluno>\n");
            }

            // Fecha a tag principal
            writer.write("</alunos>");

            writer.close();

            System.out.println("XML gravado com sucesso!");

        } catch (Exception e) {

            System.out.println("Erro ao gravar XML: " + e.getMessage());

        }
    }

    // Método para mostrar o conteúdo do XML
    public static void mostrarXML() {

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

            System.out.println("Erro ao ler XML: " + e.getMessage());

        }
    }
}
