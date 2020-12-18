import pygame


class GameOver(pygame.sprite.Sprite):
    def __init__(self, pos, image, *group):
        super(GameOver, self).__init__(*group)
        self.image = pygame.image.load('data/{}'.format(image))
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(pos)
        self.speed = 1

    def run(self):
        self.pos.x += self.speed


pygame.init()

pygame.display.set_caption("Test")
screen = pygame.display.set_mode([600, 300])
screen.fill(pygame.Color('blue'))
gameover = GameOver((-600, 0), 'gameover.png')
running = True
Clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
    if gameover.pos.x < 0:
        gameover.run()
    screen.fill(pygame.Color('blue'))
    screen.blit(gameover.image, (gameover.pos[0], gameover.pos[-1]))
    pygame.display.flip()
    Clock.tick(200)
