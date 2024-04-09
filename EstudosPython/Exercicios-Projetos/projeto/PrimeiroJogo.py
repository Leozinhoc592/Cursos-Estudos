import pygame
import sys


impulso = 0
agora = 0
jump = False
socoCont = 0
tempo = 1000
last = pygame.time.get_ticks()
clock = pygame.time.Clock()
ki = 0
sjmode = 0 
aucont = 0
#// cordenadas //
x = 400  # personagem principal DIREITA ESQUERDA
y = 400  # personagem principal CIMA BAIXO
xy = pygame.display.set_mode((x, y))
bx= 600  # inimgo DIREITA ESQUERDA
by = 400 # inimigo principal CIMA BAIXO
ls = 900 # laser DIREITA ESQUERDA
lr = 900 # laser CIMA BAIXO
gx = 900 # genki CIMA BAIXO
gy = 900 # genki DIREITA ESQUERDA
barrax = 10 # mana CIMA BAIXO
barray = 10 # mana DIREITA ESQUERDA
#/////////////////////////////////////
#//MODOS//
pulo = 0
direction = 0
cc= 0
velocidadex = 10
velocidadey = 10
#contadores ////
contador = 0
cooldown = 500   # mana da skill
genkicontX = 1
genkicontY = 1     
genkimode = 0      # genki ativa
contgenkperdido = 1 # tempo perdido sem carregar genki
genkifinal = 0
contgenkfinal = 0 # quando ela parar de andar para frente e sumir
contgenklugarxy = 0  #ajustar a genki para longe do boneco
ladogenki = 0 # manter a genki no mesmo lado
#/////////////////////
fundo = pygame.image.load('backe.jpg')
personagem = pygame.image.load('Boneco.png')
inimigo = pygame.image.load('Inimigo.png')
laser = pygame.image.load('Laser.png')
Aura1 = pygame.image.load('Aura1.png')
barra = pygame.image.load('Barra0.png')
genki = pygame.image.load('genki.png')
win_altura = 800
win_largura = 600
win = pygame.display.set_mode((win_altura,win_largura))
pygame.display.set_caption("imagensrimeiro jogo")
janela_aberta = True


while janela_aberta :
    pygame.time.delay(40)
    print(genkimode)

   # TESTE
    if ladogenki == 1 and genkifinal == 1:
            gx -= velocidadex
            contgenkfinal += 1
            gy += 3

    elif ladogenki == 2 and genkifinal == 1:
            gx += velocidadex
            gy += 3
            contgenkfinal += 1
    if genkimode == 0:
       contgenkperdido = 1
    contgenklugarxy += 1
    if genkimode == 1:
        contgenkperdido -= 1.9
    if contgenkperdido < 0:
       contgenkperdido = 0
    if contgenkperdido == 0:    
       genkifinal = 1
    if genkifinal == 1:
       
       if ladogenki == 0:
         if direction == 0:
            ladogenki = 1
         elif direction == 1:
            ladogenki = 2
            
    if contgenkfinal >= 20:
       genkimode = 2
       if contgenkfinal >= 60:
        genkimode = 3
        ladogenki = 0
        
    if genkimode == 3:
        personagem = pygame.image.load('boneco1.png')
        genkimode = 0
        genkifinal = 0
        contgenkfinal = 0
        genkicontX = 0
        genkicontY = 0
        genki = pygame.transform.scale(genki,(0,0))
          

 #//////inimigo

            








 # //////////
#personagem

    if impulso > 0:
       impulso -= 1         
    if pulo == y:
        pulo = 0
    if cooldown >= 500:
      if cc == 0:
          ls += velocidadex
          apr = 1
      elif cc == 1:
          ls -= velocidadex
          apr = 0
    if apr == 0:
        ls -= velocidadex * 10
        if ls <= -60:
            laser = pygame.image.load('invisivel.png')
    else:
        ls += velocidadex * 10
        if ls <= 0:
            laser = pygame.image.load('invisivel.png')

    if sjmode == 0:
        if direction == 1:
            personagem = pygame.image.load('boneco.png')
        else:
            personagem = pygame.image.load('boneco1.png')
    elif sjmode == 1:
        if direction == 1:
            personagem = pygame.image.load('bonecosj.png')
        else:
            personagem = pygame.image.load('boneco1sj.png')


    if genkimode == 1:
        personagem = pygame.image.load('carregandogenki.png')
    if ladogenki == 1:
        personagem = pygame.image.load('jogandogenki.png')
    if ladogenki == 2:
        personagem = pygame.image.load('jogandogenki.png')
        


    #ki e sj
    if ki < 0:
        ki = 0
    if ki == 1000:
        personagem = pygame.image.load('Explosao1.png')
        personagem = pygame.image.load('Explosao2.png')
        personagem = pygame.image.load('Explosao3.png')
        personagem = pygame.image.load('Explosao4.png')
        personagem = pygame.image.load('Explosao5.png')
        sjmode = 1
    if ki == 0:
        sjmode = 0
    if sjmode == 1:
        ki -= 2
        cooldown == 500
      
    #mana
    if sjmode == 1:
        barra = pygame.image.load('Barrasj.png')
    elif sjmode == 0:
        if cooldown < 50:
            barra = pygame.image.load('Barra0.png')
        elif cooldown >= 50 and cooldown <= 100:
            barra = pygame.image.load('Barra1.png')
        elif cooldown >= 101 and cooldown <= 200:
            barra = pygame.image.load('Barra2.png')
        elif cooldown >= 201 and cooldown <= 300:
            barra = pygame.image.load('Barra3.png')
        elif cooldown >= 301 and cooldown <= 400:
            barra = pygame.image.load('Barra4.png')
        elif cooldown > 400:
            barra = pygame.image.load('Barra5.png')
        
        inimigo = pygame.image.load('Inimigo.png')

        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidadey
    if comandos[pygame.K_DOWN]:
        y+=velocidadey
    if comandos[pygame.K_RIGHT] and impulso <= 0 or comandos[pygame.K_RIGHT] and jump == True:
        direction = 1
        if sjmode == 0:
            if contador <= 3 :
                x+= velocidadex
                if jump == False:
                 personagem = pygame.image.load('bonecoF.png')
                else:
                 personagem = pygame.image.load('bonecoP.png')
                contador+= 1
                cc = 0
            elif contador <= 5:
                if jump == False:
                 personagem = pygame.image.load('bonecoFF.png')
                else:
                 personagem = pygame.image.load('bonecoP.png')
                x+= velocidadex
                contador+= 1
                cc = 0
            elif contador >= 6 and contador <= 10:
                if jump == False:
                 personagem = pygame.image.load('bonecoFF.png')
                else:
                 personagem = pygame.image.load('bonecoP.png')
                x+= velocidadex
                contador+= 1
                cc = 0
            else:
                personagem = pygame.image.load('boneco.png')
                contador = 0
                cc = 0

        if sjmode == 1:
            if contador <= 3:
                x+= velocidadex
                if jump == False:
                 personagem = pygame.image.load('bonecoFsj.png')
                else:
                 personagem = pygame.image.load('bonecoPsj.png')
                contador+= 1
                cc = 0
            elif contador <= 5:
                if jump == False:
                 personagem = pygame.image.load('bonecoFFsj.png')
                else:
                 personagem = pygame.image.load('bonecoPsj.png')
                x+= velocidadex
                contador+= 1
                cc = 0
            elif contador >= 6 and contador <= 10:
                if jump == False:
                 personagem = pygame.image.load('bonecoFFFsj.png')
                else:
                 personagem = pygame.image.load('bonecoPsj.png')
                x+= velocidadex
                contador+= 1
                cc = 0
            else:
                personagem = pygame.image.load('bonecosj.png')
                contador = 0
                cc = 0 
    if comandos[pygame.K_LEFT] and impulso <= 0 or comandos[pygame.K_LEFT] and jump == True:
        direction = 0
        cc = 1
        if sjmode == 0:
            if contador <= 3:
                x-= velocidadex
                if jump == False:
                 personagem = pygame.image.load('bonecoL.png')
                else:
                 personagem = pygame.image.load('bonecoP1.png')
                contador+= 1
                cc = 1
            elif contador <= 5:
                if jump == False:
                 personagem = pygame.image.load('bonecoLL.png')
                else:
                 personagem = pygame.image.load('bonecoP1.png')
                x-= velocidadex
                contador+= 1
                cc = 1
            elif contador >= 6 and contador <= 10:
                if jump == False:
                 personagem = pygame.image.load('bonecoLLL.png')
                else:
                 personagem = pygame.image.load('bonecoP1.png')
                x-= velocidadex
                contador+= 1
                cc = 1
            else:
                personagem = pygame.image.load('boneco1.png')
                contador = 0
                cc = 1
        if sjmode == 1:
            if contador <= 3:
                x-= velocidadex
                if jump == False:
                 personagem = pygame.image.load('bonecoLsj.png')
                else:
                 personagem = pygame.image.load('bonecoP1sj.png')
                contador+= 1
                cc = 1
            elif contador <= 5:
                if jump == False:
                 personagem = pygame.image.load('bonecoLLsj.png')
                else:
                 personagem = pygame.image.load('bonecoP1sj.png')
                x-= velocidadex
                contador+= 1
                cc = 1
            elif contador >= 6 and contador <= 10:
                if jump == False:
                 personagem = pygame.image.load('bonecoLLLsj.png')
                else:
                 personagem = pygame.image.load('bonecoP1sj.png')
                x-= velocidadex
                contador+= 1
                cc = 1
            else:
                personagem = pygame.image.load('boneco1sj.png')
                contador = 0
                cc = 1
    if jump is False and comandos[pygame.K_SPACE]:
            if direction == 1:
                if sjmode == 0:
                    personagem = pygame.image.load('descidaimpulso.png')
                elif sjmode == 1:
                   personagem = pygame.image.load('descidaimpulsosj.png')
            elif direction == 0:
                if sjmode == 0:    
                   personagem = pygame.image.load('descidaimpulso1.png')
                elif sjmode == 1:
                   personagem = pygame.image.load('descidaimpulso1sj.png')
            impulso += 2
            if impulso == 10:
                agora = pygame.time.get_ticks()
            if agora - last >= tempo:
                last = agora
                jump = True
    if jump is True:
        y -= velocidadey
        velocidadey -= 1
        if velocidadey < -10:
            jump = False
            velocidadey = 10
            personagem = pygame.image.load('descidaimpulso.png')
    if direction == 1:    
        if comandos[pygame.K_LCTRL]:
            if sjmode == 0:    
                if socoCont <= 9:
                    personagem = pygame.image.load('ataqueD.png')
                    socoCont+=1
                elif socoCont >= 10:
                    personagem = pygame.image.load('socoD.png')
                    socoCont+=1 
                if socoCont == 20:
                    personagem = pygame.image.load('ataqueD.png')
                    socoCont = 0
            if sjmode == 1:    
                if socoCont <= 9:
                    personagem = pygame.image.load('ataqueDsj.png')
                    socoCont+=1
                elif socoCont >= 10:
                    personagem = pygame.image.load('socoDsj.png')
                    socoCont+=1 
                if socoCont == 20:
                    personagem = pygame.image.load('ataqueDsj.png')
                    socoCont = 0           
    elif direction == 0:
        if comandos[pygame.K_LCTRL]:
            if sjmode == 0:
                if socoCont <= 9:
                    personagem = pygame.image.load('ataqueE.png')
                    socoCont+=1
                elif socoCont >= 10:
                    personagem = pygame.image.load('socoE.png')            
                    socoCont+=1 
                if socoCont == 20:
                    personagem = pygame.image.load('ataqueE.png')
                    socoCont = 0
            if sjmode == 1:
                if socoCont <= 9:
                    personagem = pygame.image.load('ataqueEsj.png')
                    socoCont+=1
                elif socoCont >= 10:
                    personagem = pygame.image.load('socoEsj.png')            
                    socoCont+=1 
                if socoCont == 20:
                    personagem = pygame.image.load('ataqueEsj.png')
                    socoCont = 0
            
    
   #       HABILIDADES /////////////////////////////////////////////////////
   #       DANO - 
    if comandos[pygame.K_LSHIFT] and comandos[pygame.K_LEFT] and sjmode == 0:

     if cooldown >= 500:
        lr = y
        ls = x
        laser = pygame.image.load('Laser.png')
        laser,(ls,lr)
        cooldown = 0
     if cooldown >= 500:
        lr = y
        ls = x
        laser = pygame.image.load('Laser.png')
        laser,(ls,lr)
        cooldown = 0
    
    if comandos[pygame.K_LSHIFT] and comandos[pygame.K_RIGHT] and sjmode == 0:
     if cooldown >= 500:
        lr = y
        ls = x
        laser = pygame.image.load('Laser.png')
        laser,(ls,lr)
        cooldown = 0

    if comandos[pygame.K_LSHIFT] and sjmode == 0:
        if sjmode == 0 and genkimode != 2:
                if genkimode == 0:
                 gx = x + 30
                 gy = y - 0
                 genkimode = 1
                if genkimode == 1:
                    if contgenklugarxy >= 3:
                       gx -= 1.4
                       gy -= 2.7
                       contgenklugarxy = 0
                    genki = pygame.image.load('genki.png')
                    genkicontX += 1
                    genkicontY += 1
                    genki = pygame.transform.scale(genki,(genkicontX,genkicontY))
                    contgenkperdido += 2


#    CARREGAMENTO DE MANA -

    if comandos[pygame.K_LALT]:
        if sjmode == 0:    
            if direction == 1:
                if aucont <= 4:
                    personagem = pygame.image.load('Aura1.png') 
                    cooldown += 10
                    ki += 10
                    aucont += 1
                elif aucont > 4 and aucont < 10:
                    personagem = pygame.image.load('Aura11.png') 
                    cooldown += 10
                    ki += 10
                    aucont += 1
                elif aucont > 10 and aucont < 22:
                    personagem = pygame.image.load('Aura111.png') 
                    cooldown += 10
                    ki += 10
                    aucont += 1
                elif aucont > 20 and aucont < 26:
                    personagem = pygame.image.load('Aura1111.png') 
                    cooldown += 10
                    ki += 10
                    aucont += 1
                else:
                    personagem = pygame.image.load('Aura111.png') 
                    cooldown += 10
                    ki += 10
                    aucont = 0
            if direction == 0:
                if aucont <= 4:
                    personagem = pygame.image.load('Aura2.png') 
                    cooldown += 10
                    ki += 10
                    aucont += 1
                elif aucont > 4 and aucont < 10:
                    personagem = pygame.image.load('Aura22.png') 
                    cooldown += 10
                    ki += 10
                    aucont += 1
                elif aucont > 10 and aucont < 22:
                    personagem = pygame.image.load('Aura222.png') 
                    cooldown += 10
                    ki += 10
                    aucont += 1
                elif aucont > 22 and aucont < 26:
                    personagem = pygame.image.load('Aura2222.png') 
                    cooldown += 10
                    ki += 10
                    aucont += 1
                else:
                    personagem = pygame.image.load('Aura2222.png') 
                    cooldown += 10
                    ki += 10
                    aucont = 0
  
# //////////////////////////////////////////////////////////////////////////////////////

    


    
    
    if (x >= 800):
        x = 0
    elif (x <= 0):
        x = 800
    if (y <= 210):
        y = 210
    elif(y >= 480):
        y = 480

     
    

    win.blit(fundo,(0,0))
    win.blit(personagem,(x,y))
    win.blit(inimigo,(bx,by))
    win.blit(laser,(ls,lr))
    win.blit(barra,(barrax,barray))
    win.blit(genki,(gx,gy))
    pygame.display.update()
pygame.quit()