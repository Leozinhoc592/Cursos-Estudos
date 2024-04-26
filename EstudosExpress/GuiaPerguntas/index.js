const express = require("express");
const app = express();

app.set('view engine','ejs')

app.get("/",(req,res) => {
    var nome = "Léo";
    var linguagem = "Js";
    res.render("index",{
        nome: nome,
        linguagem: linguagem,
    })
})

app.listen(8000,() =>{
    console.log("teste")
})
cansado = 32;