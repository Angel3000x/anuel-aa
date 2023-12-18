import pygame
import sys

pygame.init()

screen = pygame.display.set_mode([800, 700])

pos_x = 180
pos_y = 125
speed = 10
movimiento = True

done = False

white = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

coins = 0
siete = 0
sandia = 0
melon = 0
cereza = 0
manzana = 0
bar = 0
campana = 0
barbar = 0

fondo = pygame.image.load("fondo.jpg")

naranja = pygame.image.load("naranja.jpg")
naranja = pygame.transform.scale(naranja, (60, 60))

campana = pygame.image.load("campana.jpg")
campana = pygame.transform.scale(campana, (60, 60))

bar = pygame.image.load("bar.jpg")
bar = pygame.transform.scale(bar, (60, 60))

barbar = pygame.image.load("barbar.jpg")
barbar = pygame.transform.scale(barbar, (60, 60))

manzana = pygame.image.load("manzana.jpg")
manzana = pygame.transform.scale(manzana, (60, 60))

cereza = pygame.image.load("cereza.jpg")
cereza = pygame.transform.scale(cereza, (60, 60))

melon = pygame.image.load("melon.jpeg")
melon = pygame.transform.scale(melon, (60, 60))

sandia = pygame.image.load("sandia.jpeg")
sandia = pygame.transform.scale(sandia, (60, 60))

siete = pygame.image.load("siete.png")
siete = pygame.transform.scale(siete, (60, 60))

estrella = pygame.image.load("estrella.jpeg")
estrella = pygame.transform.scale(estrella, (60, 60))

font = pygame.font.Font(None, 50)
dercha = True
paused = False
#DESDE AQUI EMPIEZO A DARLE VALOR A LOS CREDITOS Y FRUTAS
def mostrar(text, posicion, color):
    texto_renderizado = font.render(text, True, color)
    screen.blit(texto_renderizado, posicion)

cer=0
def mostrar_cer(text, posicion, color):
    texto_renderizado = font.render(text, True, color)
    screen.blit(texto_renderizado, posicion)
siete_siete = 0
def mostrar_siete_siete(text, posicion, color):
    texto_renderizado = font.render(text, True, color)
    screen.blit(texto_renderizado, posicion)

san = 0 
def mostrar_san(text, posicion, color):
    texto_renderizado = font.render(text,True, color)
    screen.blit(texto_renderizado, posicion)

mel = 0
def mostrar_mel(text, posicion, color):
    texto_renderizado = font.render(text, True,color)
    screen.blit(texto_renderizado,posicion)
man = 0
def mostrar_man(text, posicion,color):
    texto_renderizado = font.render(text, True, color)
    screen.blit(texto_renderizado,posicion)

baar = 0
def mostrar_baar(text, posicion,color):
    texto_renderizado = font.render(text, True, color)
    screen.blit(texto_renderizado,posicion)


camp = 0
def mostrar_camp(text, posicion,color):
    texto_renderizado = font.render(text, True, color)
    screen.blit(texto_renderizado,posicion)

nar= 0
def mostrar_nar(text, posicion,color):
    texto_renderizado = font.render(text, True, color)
    screen.blit(texto_renderizado,posicion)

bar_bar= 0
def mostrar_bar_bar(text, posicion,color):
    texto_renderizado = font.render(text, True, color)
    screen.blit(texto_renderizado,posicion)
    
est= 0
def mostrar_est(text, posicion,color):
    texto_renderizado = font.render(text, True, color)
    screen.blit(texto_renderizado,posicion)



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True                             
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                coins += 1
                if coins>=1000:
                    coins=999

                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_6:
                if coins>0:
                    coins-=1
                    cer+=1
                    if (coins<0 or cer>=10):
                        cer=9
                        coins+=1
                

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_9:
                if coins>0:
                    coins-=1
                    siete_siete+=1
                    if (coins<0 or siete_siete >=10):
                        siete_siete=9
                        coins+=1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_8:
                if coins >0:
                    coins -=1
                    san +=1
                    if(coins<0 or san >= 10):
                        san = 9
                        coins +=1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_7:
                if coins >0:
                    coins -=1
                    mel +=1
                    if (coins <0 or mel >=10):
                        mel = 9
                        coins +=1                       
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_5:
                if coins >0:
                    coins -=1
                    man +=1
                    if (coins <0 or man >=10):
                        man = 9
                        coins +=1 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                if coins >0:
                    coins -=1
                    baar +=1
                    if (coins <0 or baar >=10):
                        baar = 9
                        coins +=1                 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                if coins >0:
                    coins -=1
                    camp +=1
                    if (coins <0 or camp >=10):
                        camp = 9
                        coins +=1                 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if coins >0:
                    coins -=1
                    nar +=1
                    if (coins <0 or nar >=10):
                        nar = 9
                        coins +=1   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                if coins >0:
                    coins -=1
                    bar_bar +=1
                    if (coins <0 or bar_bar >=10):
                        bar_bar = 9
                        coins +=1   
                        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                if coins >0:
                    coins -=1
                    est +=1
                    if (coins <0 or est >=10):
                        est = 9
                        coins +=1 

    if movimiento:
        if pos_x < 600:
            pos_x += speed
        elif pos_y < 500:
            pos_y += speed
        else:
            movimiento = False

    else:
        if pos_x >  180:
            pos_x -= speed
        elif pos_y > 125:
            pos_y -= speed
        else:
            movimiento = True

    pygame.display.update()
    
   
    pygame.display.flip()


    screen.blit(fondo,[0,0])

#UBICACION DE CADA RECUADRO
    screen.blit(naranja,(180, 125)) 
    screen.blit(campana,(250, 125))
    screen.blit(bar,(320, 125))
    screen.blit(barbar,(390, 125))
    screen.blit(manzana,(460, 125))
    screen.blit(cereza,(530, 125))
    screen.blit(melon,(600, 125))     
    screen.blit(sandia,(600, 500))
    screen.blit(cereza,(600, 423)) 
    screen.blit(manzana,(600, 345))
    screen.blit(cereza,(600, 270))
    screen.blit(naranja,(600, 190)) 
    screen.blit(campana,(530, 500))
    screen.blit(cereza,(460, 500))
    screen.blit(siete,(390, 500))
    screen.blit(manzana,(320, 500))
    screen.blit(cereza,(250, 500)) 
    screen.blit(estrella,(180, 500))
    screen.blit(melon,(180, 420))
    screen.blit(cereza,(180, 345))
    screen.blit(naranja,(180, 270)) 
    screen.blit(campana,(180, 200))
   
    screen.blit(bar,(1,630))
    screen.blit(barbar,(82,630))
    screen.blit(manzana,(164,630))
    screen.blit(cereza,(246,630))
    screen.blit(melon,(328,630))
    screen.blit(sandia,(410,630))
    screen.blit(siete,(492,630))
    screen.blit(naranja,(574, 630))
    screen.blit(campana,(656, 630))
    screen.blit(estrella,(739, 630))

    
    pygame.draw.rect (screen, red,(pos_x, pos_y, 60,60) ,5)

    pygame.draw.rect (screen, white,(70, 60, 250,50)) 
    pygame.draw.rect (screen, white,(455, 60, 200,50)) 

    
    pygame.draw.circle(screen, white, (30,600), 25) #bar presione la tecla 3
    mostrar_baar(f"{baar}",(20,585),(255,0,0)) 
    
    pygame.draw.circle(screen, white, (115,600), 25) #barbar presione la tecla 4
    mostrar_bar_bar(f"{bar_bar}",(105,585),(255,0,0)) 
    
    pygame.draw.circle(screen, white, (200,600), 25) #manzana presione la tecla 5
    mostrar_man(f"{man}",(190,585),(255,0,0)) 
    
    pygame.draw.circle(screen, white, (280,600), 25) #cereza presione tecla 6
    mostrar_cer(f"{cer}",(270,585),(255,0,0)) 
    
    pygame.draw.circle(screen, white, (360,600), 25) #melon presione tecla 7
    mostrar_mel(f"{mel}",(350,585), (255,0,0))

    pygame.draw.circle(screen, white, (440,600), 25) #sandia presione tecla 8
    mostrar_san(f"{san}",(430.5,585), (255,0,0))
    
    pygame.draw.circle(screen, white, (520,600), 25) #77 presione tecla 9
    mostrar_siete_siete(f"{siete_siete}",(510,585),(255,0,0)) 

    pygame.draw.circle(screen, white, (600,600), 25) #naranja presione la tecla 1
    mostrar_nar(f"{nar}",(590,585),(255,0,0)) 
    
    pygame.draw.circle(screen, white, (690,600), 25) #campana presione tecla 2
    mostrar_camp(f"{camp}",(680,585),(255,0,0)) 

    pygame.draw.circle(screen, white, (770,600), 25) #estrella presione tecla 0
    mostrar_camp(f"{est}",(760,585),(255,0,0)) 
 
    if coins >= 0:
        mostrar(f"creditos: {coins}", (70, 70), (0, 0, 0))
    else:
        mostrar(f"creditos: 0", (70, 70), (0, 0, 0))

    mostrar(f"premios: ", (460, 70), (0, 0, 0))

    pygame.display.flip()

pygame.quit()
sys.exit()
