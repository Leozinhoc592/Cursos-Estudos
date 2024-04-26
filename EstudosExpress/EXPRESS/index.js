const express = require("express");
const app = express();

app.get("/",function(req,res){
    res.send("Olá")
})
app.get("/blog/:artigo?",function (req,res){

    var artigo = req.params.artigo
    if(artigo){
        res.send("Artigo: " + artigo)
    }else{
        res.send("Bem vindo teste")
    }
})

app.listen(4000,function (erro){
    if(erro){
        console.log("Ocorreu um erro")
    }else {
        console.log("Servidor iniciado com sucesso")
    }

})