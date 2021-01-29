import pygame, os, sys


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


class GameHero(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image_list = []
        self.image_list.append(self.load_image("Hero_Front.png"))
        self.image_list.append(self.load_image("Hero_Back.png"))
        self.image_list.append(self.load_image("Hero_Left.png"))
        self.image_list.append(self.load_image("Hero_Right.png"))
        self.image_list.append(self.load_image("HeroGo.png"))
        self.image_list.append(self.load_image("HeroGoLeft.png"))
        self.image = self.load_image("Hero_Front.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def turn_right(self):
        return self.image_list[3]

    def turn_left(self):
        return self.image_list[2]

    def turn_back(self):
        return self.image_list[1]

    def turn_forward(self):
        return self.image_list[0]

    def go_right(self):
        return self.image_list[4]

    def go_left(self):
        return self.image_list[5]

    def load_image(self, name, colorkey=None):
        fullname = os.path.join(name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_w:
                self.image = self.turn_back()
                self.rect = self.rect.move(0, -5)

            if args[0].key == pygame.K_a:
                self.image = self.turn_left()
                self.rect = self.rect.move(- 5, 0)

            if args[0].key == pygame.K_s:
                self.image = self.turn_forward()
                self.rect = self.rect.move(0, 5)

            if args[0].key == pygame.K_e:
                self.image = self.turn_right()
                self.rect = self.rect.move(5, 0)


if __name__ == '__main__':
    fps = 60
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    all_sprites.add(GameHero(10, 10))
    while running:
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                all_sprites.update(event)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
