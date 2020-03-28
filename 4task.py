import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
screen.fill(white)
pygame.draw.arc(screen, black,(0,0,2560/2,1920/2),0, 2*3.14, 1)
pygame.draw.lines(screen, pink, False, [(0,480),(640,0)])
clock = pygame.time.Clock()

running = True

FPS= 30 
playtime = 0.0

while running:
    milliseconds = clock.tick(FPS) 
    playtime += milliseconds / 1000.0 

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
    text = "FPS {0}".format(FPS) +" Playtime : {0:.2f}" .format(playtime)   
    pygame.display.set_caption(text)   
    pygame.display.flip()

pygame.display.update()