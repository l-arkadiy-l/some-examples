import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, pos, image, *group):
        super(Hero, self).__init__(*group)
        self.image = pygame.image.load('data/{}'.format(image))
        self.pos = pygame.Vector2(pos)
        self.rect = self.image.get_rect()
        self.vel = pygame.Vector2((0, 0))
        self.speed = 10

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.vel.x = self.speed
            if event.key == pygame.K_LEFT:
                self.vel.x = -self.speed
            if event.key == pygame.K_UP:
                self.vel.y = -self.speed
            if event.key == pygame.K_DOWN:
                self.vel.y = self.speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and self.vel.x > 0:
                self.vel.x = 0
            elif event.key == pygame.K_LEFT and self.vel.x < 0:
                self.vel.x = 0
            elif event.key == pygame.K_UP:
                self.vel.y = 0
            elif event.key == pygame.K_DOWN:
                self.vel.y = 0

    def update_pos(self):
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y


pygame.init()

pygame.display.set_caption("Hero is moving!")
SIZE = 300
screen = pygame.display.set_mode((SIZE, SIZE))
screen.fill(pygame.Color('white'))
hero = Hero((0, 0), 'creature.png')
running = True
Clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        hero.move(event)
    hero.update_pos()
    print(hero.pos)
    screen.fill(pygame.Color('white'))
    screen.blit(hero.image, (hero.pos[0], hero.pos[-1]))
    pygame.display.flip()
    Clock.tick(10)
