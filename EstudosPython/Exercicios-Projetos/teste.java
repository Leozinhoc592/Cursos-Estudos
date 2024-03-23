import java.util.Scanner;
import java.util.Random;
public class teste {

    public static void main(String args[]){
      String inas = new String("aaa");
      Scanner teclado = new Scanner(System.in);
      do {
        int escolhaC = 0;
        String escolha = teclado.nextLine();
        if (escolha == "papel"){
          escolhaC = 1;
        } else if (escolha == "tesoura"){
          escolhaC = 2;
        } else {
          escolhaC = 3;
        }
        /*pedra = 1
         *papel = 2 
         *tesoura = 3
         */
        int[] intArray = {1, 2, 3};
        int escolhainimigo = new Random().nextInt(intArray.length);
        
        if (escolhainimigo == 1){
          if (escolhaC == 1){
            System.out.print("Empate");
          } else if (escolhaC == 2){
            System.out.print("Derrota");
          } else {
            System.out.print("Vitoria");
          }
        } else if (escolhainimigo == 2) {
          if (escolhaC ==1){
            System.out.print("Vitoria");
          } else if (escolhaC ==2){
            System.out.print("Empate");
          } else {System.out.print("derrota");
        }
        } else {
          if (escolhaC ==3){
            System.out.print("Derrota");
          } else if (escolhaC ==2){
            System.out.print("Vitoria");
          } else {System.out.print("Empate");
        }

        }
        String inas = teclado.nextLine();
      } while (inas != "aaa");

    }
}