package cursojava;
import java.util.Scanner;

public class teste {
    public static void main(String args[]){
      Scanner leitor = new Scanner(System.in);
      System.out.printf("Informe um numero:\n");
      int preco = leitor.nextInt();
      System.out.printf("Valor informado %d",preco);
    }
}