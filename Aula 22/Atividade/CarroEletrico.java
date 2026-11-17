public class CarroEletrico extends Veiculo {

  public CarroEletrico(String modelo) {
    super(modelo);
  }

  @Override
  public void ligarMotor(){
    System.out.println("Sistema elétrico ligado!");
  }

  public String carregarBateria(){
      return "Carregando na estação rápida";
  }
}
