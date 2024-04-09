const canvas = document.querySelector('canvas')
const c = canvas.getContext('2d')

console.log(colisao);

canvas.width = 1024;
canvas.height = 576;

const colisaoMapa = []
const offset = {
    x: -780,
    y: -550
}
for (let i = 0;i < colisao.length; i+=70){
    colisaoMapa.push(colisao.slice(i, 70 + i))
}
class Limite {
    static width = 48
    static height = 48
    constructor({posicao}) {
        this.posicao = posicao
        this.width = 48
        this.height = 48
    }

    draw() {
        c.fillStyle = 'red'
        c.fillRect(this.posicao.x,this.posicao.y,this.width,this.height)
    }
}

const limites = []

colisaoMapa.forEach((row,i) => {
    row.forEach((symbol,j) => {
        if (symbol === 1025)
            limites.push(
                new Limite({
                    posicao: {
                        x: j * Limite.width + offset.x,
                        y: i * Limite.height + offset.y
                }
            })
        )
    })
})
console.log(limites)

const imagem = new Image();
imagem.src = './imagens/ILHA.png'

const imagemJogador = new Image()
imagemJogador.src = './imagens/JogadorBaixo.png'

class Sprite {
    constructor({posicao,velocidade,imagem,frames = {max:1}}){
        this.posicao = posicao
        this.imagem = imagem
        this.frames = frames
    }

    draw() {
        c.drawImage(
            this.imagem,
            0,
            0,
            this.imagem.width / this.frames.max,
            this.imagem.height,
            this.posicao.x,
            this.posicao.y,
            this.imagem.width / this.frames.max,
            this.imagem.height
        )
    }
}

const jogador = new Sprite ({
    posicao: {
        x: canvas.width / 2 - 192 / 4 / 2,
        y: canvas.height / 2 - 68 / 2
    },
    imagem: imagemJogador,
    frames:{
        max:4
    }
})

const background = new Sprite({
    posicao: {
        x: offset.x,
        y: offset.y
    },
    imagem: imagem
})
const keys = {
w: {
    pressed: false
},
a: {
    pressed: false
},
s: {
    pressed: false
},
d: {
    pressed: false
}
}
const testeLimite = new Limite({
    posicao:{
        x:400,
        y:400
    }
})
const moveis = [background,testeLimite]
function animacao() {
  window.requestAnimationFrame(animacao)
  background.draw()
  //limites.forEach(Limite => {
   // Limite.draw()
  //})
  jogador.draw()
    

    if (keys.w.pressed && ultimaTecla === 'w'){ 
        moveis.forEach((moveis) =>{
            moveis.posicao.y += 3
        })
    }else if (keys.a.pressed && ultimaTecla === 'a') {
        moveis.forEach((moveis) =>{
            moveis.posicao.x += 3
        }) 
    }else if (keys.s.pressed && ultimaTecla === 's') {
        moveis.forEach((moveis) =>{
            moveis.posicao.y -= 3
        })
    }else if (keys.d.pressed && ultimaTecla === 'd')
    {moveis.forEach((moveis) =>{
        moveis.posicao.x -= 3
    })}
}
animacao()

let ultimaTecla = ''
window.addEventListener ('keydown', (e) => {
    switch(e.key) {
        case 'w':
            keys.w.pressed = true
            ultimaTecla = 'w'
            break
        case 'a':
            keys.a.pressed = true
            ultimaTecla = 'a'
            break
        case 's':
            keys.s.pressed = true
            ultimaTecla = 's'
            break
        case 'd':
            keys.d.pressed = true
            ultimaTecla = 'd'
            break           

    }
    console.log(keys)

})
window.addEventListener ('keyup', (e) => {
    switch(e.key) {
        case 'w':
            keys.w.pressed = false
            break
        case 'a':
            keys.a.pressed = false
            break
        case 's':
            keys.s.pressed = false
            break
        case 'd':
            keys.d.pressed = false
            break           

    }
    console.log(keys)

})
