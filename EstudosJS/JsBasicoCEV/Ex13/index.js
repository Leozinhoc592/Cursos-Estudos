var agora = new Date()
var hora = agora.getHours()
console.log(`Agora são exatamente ${hora}horas`)
if (hora > 12 && hora < 17){
    console.log("Boa tarde")
}else if ( hora > 17 && hora < 0){
    console.log("Boa noite")
}else if ( hora > 0 && hora < 5){
    console.log("Boa madrugada")
}else{
    console.log("Bom dia")
}