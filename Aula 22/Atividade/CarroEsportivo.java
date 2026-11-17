public class CarroEsportivo extends Veiculo {

  public CarroEsportivo(String modelo) {
    super(modelo);
  }

  @Override
  public void ligarMotor(){
    System.out.println("Motor ligado!");
  }

  public String ativarTurbo(){
      return "Turbo ativado!";
  }
}
