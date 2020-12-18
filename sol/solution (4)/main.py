import random

import pygame


class Boom(pygame.sprite.Sprite):
    def __init__(self, pos, image, *group):
        super(Boom, self).__init__(*group)
        self.image = pygame.image.load('data/{}'.format(image))
        # self.image.fill(pygame.Color('red'))
        self.pos = pygame.Vector2(pos)
        self.rect = self.image.get_rect()
        print(self.rect.width)
        self.image_boom = pygame.image.load('data/boom.png')

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom


pygame.init()

pygame.display.set_caption("Hero is moving!")
SIZE = WIDTH, HEIGHT = (500, 500)
screen = pygame.display.set_mode(SIZE)
all_sprites = pygame.sprite.Group()
for i in range(20):
    # можно сразу создавать спрайты с указанием группы
    bomb = Boom((0, 0), 'bomb.png')
    # задаём случайное местоположение бомбочке
    bomb.rect.x = random.randrange(WIDTH - bomb.rect.width)
    bomb.rect.y = random.randrange(HEIGHT - bomb.rect.height)
    all_sprites.add(bomb)

running = True
flipping = False
Clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        all_sprites.update(event)

    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)

    # screen.fill(pygame.Color('white'))
    # screen.blit(bomb.image, (bomb.pos[0], bomb.pos[-1]))
    pygame.display.flip()
    Clock.tick(60)
