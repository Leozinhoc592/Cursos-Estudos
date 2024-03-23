class Cliente {

    nome;
    cpf;
    agencia;
    saldo;

}

const cliente1 = new Cliente();
const cliente2 = new Cliente();
const cliente3 = new Cliente();

cliente1.nome = "Ricardo";
cliente1.cpf = 111130492;
cliente1.agencia = 1001;
cliente1.saldo = 32;

cliente2.nome = "Alice";
cliente2.cpf = 982314321;
cliente2.agencia = 2034;
cliente2.saldo = 7232832;

cliente2.nome = "Carlos";
cliente2.cpf = 3253221;
cliente2.agencia = 2034;
cliente2.saldo = 493200;

cliente2.nome = "Renato";
cliente2.cpf = 12341221;
cliente2.agencia = 2234;
cliente2.saldo = 423500;

console.log(cliente1);
console.log(cliente2);
console.log(cliente3);
