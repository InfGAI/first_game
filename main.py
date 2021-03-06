import pygame
import random
size = weight, height = (1000, 800)

class Ball():
    def __init__(self, pos, color):
        self.pos = pos  # (100,100)
        self.color = color
        self.dir = list(random.choices(range(-4, 5), k=2))
        pygame.draw.circle(screen, self.color, self.pos, 50)

    def hmove(self):
        x, y = self.pos
        if x + 25 >= weight or x - 25 <= 0:
            self.dir[0] *= -1
        if y + 25 >= height or y - 25 <= 0:
            self.dir[1] *= -1
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])

    def renew(self):
        pygame.draw.circle(screen, self.color, self.pos, 20)

pygame.init()
FPS = 50
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
ball_list=[]
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            r, g, b = random.choices(range(0, 256), k=3)
            if event.button == 3:
                ball_list.append(Ball((x, y), (r, g, b)))

    screen.fill((255, 0, 0))
    for ball in ball_list:
        ball.renew()
        ball.hmove()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()