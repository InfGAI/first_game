import pygame
class Ball():
    def __init__(self,pos,color):
        self.pos=pos # (100,100)
        self.color=color
        pygame.draw.circle(screen, self.color, self.pos, 50)

    def hmove(self):
        self.pos=(self.pos[0]+1,self.pos[1])

    def renew(self):
        pygame.draw.circle(screen, self.color, self.pos, 50)

pygame.init()
FPS=50
screen=pygame.display.set_mode((600,300))
clock=pygame.time.Clock()
first_ball=Ball((100,100),(0,0,0))
second_ball=Ball((500,100),(0,255,0))
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((255, 0, 0))
    first_ball.renew()
    first_ball.hmove()
    second_ball.renew()
    second_ball.hmove()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()