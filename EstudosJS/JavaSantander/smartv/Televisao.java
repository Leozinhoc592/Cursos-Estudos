package smartv;

public class Televisao {
    
    private boolean ligada = false;
    private int canal = 1;
    private int volume;



    public boolean getLigada(){
        return ligada;
    }
    public int getCanal(){
        return canal;
    }
    public int getVolume(){
        return volume;
    }
    public void setLigada(boolean Ligada){
        this.ligada = Ligada;
    }
    public void setCanal(int Canal){
        this.canal = Canal;
    }
    public void setVolume(int Volume){
        this.volume = Volume;
    }
    public void Power(){
        if (this.ligada){
            this.ligada = false;
        }else{
            this.ligada = true;
        }   
    }

    public void Aumentar(int valor){
        this.volume += valor;
    }
    public void Diminuir(int valor){
        this.volume -= valor;
    }

    public void MudarCanal(int valor){
        switch (valor){
            case 1:
                this.canal += 1;
                break;
            case -1:
                this.canal -= 1;
                break;
            default:
                this.canal = valor;
                break;
        }
        
    }

    public String mostrar(){
        return ("Ligada: " + getLigada() + ", Canal: " + getCanal() + ", Volume: " + getVolume());
    }

}
