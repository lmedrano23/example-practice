import pygame
import random 

#set variables:
screenDimensions = (800,600)
backgroundColor = (135, 206, 235)
birdX = 400
birdY = 400
birdY_change = 0

pipeX = 170
pipeHeight = random.randint(50,300)

#create the screen:

screen = pygame.display.set_mode(screenDimensions)

#scene title:
pygame.display.set_caption("Flappy Bird")

#playable character function:
def player(x,y):
    pygame.draw.rect(screen, (255,0,0),(x,y,20,25))

#def pipes(x):
    #pygame.draw.rect(screen, (0, 255, 0),(x,20,50,50))
    #if(x > 0):
     #   x -= 0.5
    #elif(x >= 0):
     #   x = 800
    #pygame.draw.rect(screen, (0, 255, 0),(x,20,50,50))



running = True

while running:
    #RGB color for background color: 
    screen.fill(backgroundColor)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Checks for pressed keys then adjusts character coords based on pressed keys:
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                birdY_change = -0.2
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                birdY_change = 0.2   


    birdY += birdY_change

    #restrctions to movement within canvas:
    if birdY <= 50:
        birdY = 50
    elif birdY >= 575:
        birdY = 575

    if(pipeX > 0):
        pipeX -= 0.2
    if(pipeX < 0):
        pipeX = 800
        pipeHeight = random.randint(50,300)

    pygame.draw.rect(screen, (0, 255, 0),(pipeX,0,50,pipeHeight))


    player(birdX,birdY)
    #pipes(710)
    pygame.display.update()