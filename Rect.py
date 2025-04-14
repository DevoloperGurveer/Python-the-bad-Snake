import pygame
pygame.init()
screen=pygame.display.set_mode((690,420))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(100,89,88),pygame.Rect(100,100,69,69))
    Lavender=(210,0,200)
    pygame.draw.circle(screen,Lavender,(230,240),55)
    pygame.draw.circle(screen,Lavender,(200,210),50,5)
    pygame.display.flip()