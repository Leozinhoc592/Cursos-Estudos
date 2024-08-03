package smartv;


public class ClassePrincipal{
public static void main(String[] args){

    var teve = new Televisao();


    teve.MudarCanal(-1);
    teve.MudarCanal(-1);
    teve.MudarCanal(-1);
    teve.MudarCanal(500);
    teve.Power();
    teve.Power();

    System.out.println(teve.mostrar());
    


}
}
