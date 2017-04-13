import pygame
import sys
import time
import random
from pygame.locals import *

icon= pygame.image.load('gapple.png')
pygame.display.set_icon(icon)
#INICIA EL JUEGO#
pygame.init()
pygame.mixer.music.load("Malmen_-_Flowers.wav")
pygame.mixer.music.play(1)
#INDICA EL TAMANO DE LA VENTANA#
ventana = pygame.display.set_mode((700,500))
#INDICA EL TITULO DE LA VENTANA#
pygame.display.set_caption("Snake")

display_width=800
display_height=600




clock = pygame.time.Clock()

font=pygame.font.SysFont(None, 35)

#pantalla de incicio
def game_intro():
    intro = True

    myfont= pygame.font.SysFont('Comic Sans', 50)
    myfont2= pygame.font.SysFont('Comic Sans', 30)
    myfont3= pygame.font.SysFont('Comic Sans', 41)
    text=myfont.render('      Welcome to my snake game ',False,(0, 251, 33))
    text2=myfont2.render('  Just go and eat all the apples you see',False,(255,255,255))
    instruction=myfont2.render('If you eat yourself you die, you know... like in real life',False,(255, 255, 255))
    instruction2=myfont2.render(' If you go out of screen you die, this is not pacman >:(',False,(255, 255, 255))



    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    intro=False


                if event.key == K_q:
                    pygame.quit()
                    sys.exit()



        ventana.fill((0,0,0))
        ventana.blit(text,(60,170))
        ventana.blit(text2,(140,210))
        ventana.blit(instruction,(90,250))
        ventana.blit(instruction2,(80,280))
        ventana.blit(myfont3.render("    Press C to start or Q to quit",False,(255, 0, 0)),(125,320))
        pygame.display.update()
        clock.tick(15)


def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    ventana.blit(screen_text, [display_height/2 - screen_text.get_width()/2.6, display_height/2.5])


def snake(block,snakelist,head):
    #dibujando snake#
    #snakelist me guarda una posicion x y una posicion y
    ventana.blit(head, (snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(ventana,(5, 42, 8),[XnY[0],XnY[1],block,block])


def gameLoop():

    puntos=0
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=0
    lead_y_change=0
    block_size=10
    FPS=15
    gameOver=False
    snakeList=[]
    snakeLength=1
    direction= 270
    img= pygame.image.load('snake.png')
    head=img
    apple=pygame.image.load('gapple.png')
    scorefont= pygame.font.SysFont('Comic Sans', 30)
    effect = pygame.mixer.Sound('pickup.wav')



    #up = 0 left = 90 down = 180 right = 270

    randAppleX=random.randrange(20,display_width-100,10)
    randAppleY=random.randrange(20,display_height-100,10)

    while True:
        while gameOver == True:
            ventana.fill((0, 0, 0))
            message_to_screen('YOU LOSE press C to continue or Q to quit', (255, 0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_q:
                        gameOver= False
                        pygame.quit()
                    elif event.key == pygame.K_c:
                        gameLoop()
        #manejador de eventos#
        for event in pygame.event.get():
            #quit#
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #movimiento#
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    head=pygame.transform.rotate(img,90)
                elif event.key==pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    head=pygame.transform.rotate(img,270)
                elif event.key==pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    head=pygame.transform.rotate(img,0)
                elif event.key==pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    head=pygame.transform.rotate(img,180)
            #if event.type == pygame.KEYUP:
                #if event.key == pygame.K_RIGHT or event.key==pygame.K_LEFT:
                #    lead_x_change = 0
                #if event.key == pygame.K_UP or event.key==pygame.K_DOWN:
                    #lead_y_change = 0

        if  lead_x < 0 or lead_y < 0 or  lead_x >= display_width-100 or  lead_y >= display_height-100:
            gameOver=True



        lead_x += lead_x_change
        lead_y += lead_y_change

        #agregando cordenadas a la serpiente
        snakeHead=[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        #fondo blanco#
        ventana.fill((255, 255, 255))
        #dibujando MANZANA
        AppleThickness=26
        score=scorefont.render('Score: ' + str(puntos),False,(0, 0, 0))
        ventana.blit(score,(10,10))
        #pygame.draw.rect(ventana,(255, 0, 0),[randAppleX,randAppleY,AppleThickness,AppleThickness])
        ventana.blit(apple,(randAppleX, randAppleY))
        #dibujando snake
        snake(10,snakeList,head)
        #pregunto si la snake se ha mordido
        if snakeHead in snakeList[:-1]:
            if snakeHead == snakeList[0]:
                continue
            gameOver = True
        #ACTUALIZA EL ESTADO DE LA VENTANA#
        pygame.display.update()




#        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
#            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
#                    #comiendo la manzana
#                    randAppleX=random.randrange(0, display_width-200,10)
#                    randAppleY=random.randrange(0, display_height-200,10)
#                    snakeLength+=1
#                    FPS+=2


        if lead_x > randAppleX and lead_x < (randAppleX + AppleThickness) or (lead_x + block_size) > randAppleX and (lead_x + block_size) <( randAppleX +AppleThickness):
            if lead_y > randAppleY and lead_y < (randAppleY + AppleThickness) or (lead_y + block_size) > randAppleY and (lead_y + block_size) <(randAppleY +AppleThickness):
                  #comiendo la manzana
                  randAppleX=random.randrange(10, 400,10)
                  randAppleY=random.randrange(10, 400,10)
                  snakeLength+=1
                  FPS+=1
                  puntos+=1
                  effect.play()


        #FPS#
        clock.tick(FPS)

game_intro()
gameLoop()
