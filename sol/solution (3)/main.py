import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self, pos, image, *group):
        super(Car, self).__init__(*group)
        self.image = pygame.image.load('data/{}'.format(image))
        self.pos = pygame.Vector2(pos)
        self.rect = self.image.get_rect()
        self.speed = 5

    def update_pos(self):
        if self.pos.x <= 0 or not flipping:
            self.pos.x += self.speed
        elif self.pos.x >= WIDTH - self.rect.width or flipping:
            self.pos.x -= self.speed


pygame.init()

pygame.display.set_caption("Hero is moving!")
SIZE = WIDTH, HEIGHT = (600, 95)
screen = pygame.display.set_mode(SIZE)
screen.fill(pygame.Color('white'))
car = Car((0, 0), 'car2.png')
running = True
flipping = False
Clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
    car.update_pos()
    screen.fill(pygame.Color('white'))
    if car.pos.x <= 0 or not flipping:
        flipping = False
        screen.blit(car.image, (car.pos[0], car.pos[-1]))
    if car.pos.x >= WIDTH - car.rect.width or flipping:
        flipping = True
        screen.blit(pygame.transform.flip(car.image, True, False), (car.pos[0], car.pos[-1]))
    pygame.display.flip()
    Clock.tick(60)
