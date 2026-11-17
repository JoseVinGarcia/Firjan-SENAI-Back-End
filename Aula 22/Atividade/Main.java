public class Main {
    public static void main(String[] args) {
      CarroEsportivo c = new CarroEsportivo("Ferrari F8");
      System.out.println("Meu carro esportivo é uma "+c.modelo);
      System.out.println("E no momento está com o seguinte status: "+c.ativarTurbo());

      CarroEletrico e = new CarroEletrico("Tesla Model S");
      System.out.println("Eu tenho um carro elétrico modelo "+e.modelo);
      System.out.println("Mas agora ele está: "+e.carregarBateria());
    }
}
