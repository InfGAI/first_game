import pygame
import random


class Ball():
    def __init__(self, pos, color):
        self.pos = pos  # (100,100)
        self.color = color
        pygame.draw.circle(screen, self.color, self.pos, 50)

    def hmove(self):
        self.pos = (self.pos[0] + 1, self.pos[1])

    def renew(self):
        pygame.draw.circle(screen, self.color, self.pos, 20)

pygame.init()
FPS=50
screen=pygame.display.set_mode((600,300))
clock=pygame.time.Clock()
ball_list=[]
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            r, g, b = random.choices(range(0, 256), k=3)
            if event.button == 1:
                ball_list.append(Ball((x, y), (r, g, b)))
            else:
                ball_list.pop(0)
    screen.fill((255, 0, 0))
    for ball in ball_list:
        ball.renew()
        ball.hmove()


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()