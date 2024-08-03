public String transferepara(double valor, Conta destino) {
    String resultadoSaque = this.sacar(valor);
    if (resultadoSaque.equals("O saque foi realizado novo saldo: " + this.saldo)) {'
        =-------
    }else {
        return "transferencia falhou saldo insuficiente";
    }

}