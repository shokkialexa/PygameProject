import pygame, os, sys

import PyGameProjectSpriteMove

pygame.init()
size = width, height = 45 * 16, 18 * 16
user_group = pygame.sprite.Group()
board_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
pokemons_group = pygame.sprite.Group()


def load_image(filename):
    fullname = os.path.join(f"Data/{filename}")
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def pokeball(x, y):
    pokeball = pygame.sprite.Sprite()
    pokeball.image = load_image("pokeball.png")
    pokeball.rect = pokeball.image.get_rect()
    pokeball.rect.x = x
    pokeball.rect.y = y
    return pokeball


def start_screen():
    intro_text = ["Правила игры:",
                  "Чтобы отрыть меню, ",
                  "нажмите 5 посередине между стрелками",
                  "Чтобы закрыть отрываюшиеся окна,",
                  " кликните мышью ",
                  "или нажмите кнопку на клавиатуре",
                  "Передвигайтесь клавишами стрелок",
                  "Если вы хотите начать, кликните мышью!"]
    size_for_start_screen = 600, 600
    screen = pygame.display.set_mode(size_for_start_screen)
    screen.fill((0, 0, 0))
    pikachu_group = pygame.sprite.Group()
    pikachu = pygame.sprite.Sprite(pikachu_group)
    pikachu.image = load_image("fon.png")
    pikachu.rect = pikachu.image.get_rect()
    pikachu.rect.x, pikachu.rect.y = 200, 200
    pikachu_group.draw(screen)
    font = pygame.font.Font(pygame.font.match_font('cambria'), 20)
    string_rendered = font.render("Добро пожаловать в игру Pokemon Searching!", True, pygame.Color('white'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 20
    screen.blit(string_rendered, intro_rect)
    text_coord = 50
    for line in intro_text:
        font = pygame.font.Font(pygame.font.match_font('cambria'), 15)
        string_rendered = font.render(line, False, (244, 164, 96))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.flip()
        clock.tick(fps)


def menu(user, menu_screen):
    pokemons = user.get_pokemons()
    menu_screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 25)
    string_rendered = font.render(f"Your pokemons:", True, pygame.Color('white'))
    string_rect = string_rendered.get_rect()
    string_rect.x = 50
    string_rect.y = 30
    menu_screen.blit(string_rendered, string_rect)
    dx = 50
    dy = 50
    for i in range(len(pokemons)):
        pokemons[i].set_rect(i * 70 + dx, dy)
        font = pygame.font.Font(None, 15)
        ev, sk = pokemons[i].get_information()
        string_rendered = font.render(f"evolution: {ev}", False, (240, 230, 140))
        string_rect = string_rendered.get_rect()
        string_rect.x = i * 70 + dx
        string_rect.y = 60 + dy
        menu_screen.blit(string_rendered, string_rect)
        string_rendered = font.render(f"skill: {sk}", False, (240, 230, 140))
        string_rect.x = i * 70 + dx
        string_rect.y = 70 + dy
        menu_screen.blit(string_rendered, string_rect)
        pokemons_group.add(pokemons[i])
    clock = pygame.time.Clock()
    if not pokemons:
        font = pygame.font.Font(None, 25)
        string_rendered = font.render(f"You haven't any pokemons", 1, pygame.Color('white'))
        string_rect = string_rendered.get_rect()
        string_rect.x = 70
        string_rect.y = 70
        menu_screen.blit(string_rendered, string_rect)
    number = user.get_pokeballs()
    font = pygame.font.Font(None, 25)
    string_rendered = font.render(f"Your pokeballs:", 1, pygame.Color('white'))
    string_rect = string_rendered.get_rect()
    string_rect.x = 50
    string_rect.y = 130
    menu_screen.blit(string_rendered, string_rect)
    pokeball_for_menu = pokeball(50, 150)
    pokeballs_group = pygame.sprite.Group()
    pokeballs_group.add(pokeball_for_menu)
    font = pygame.font.Font(None, 15)
    string_rendered = font.render(f"number:{number}", False, (240, 230, 140))
    string_rect = string_rendered.get_rect()
    string_rect.x = 50
    string_rect.y = 190
    menu_screen.blit(string_rendered, string_rect)
    while True:
        pokemons_group.draw(menu_screen)
        pokeballs_group.draw(menu_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.flip()
        clock.tick(fps)


def get_something(screen, something):
    new_screen = screen
    font = pygame.font.Font(None, 25)
    new_screen.fill((184, 134, 11))
    string = font.render("You get:", 1, (110, 50, 19))
    rect = (110, 70, 25, 25)
    new_screen.blit(string, rect)
    try:
        str(something)
        if something == "pokeball":
            pokeball_for_smth = pokeball(150, 110)
            pokeballs_group = pygame.sprite.Group()
            pokeballs_group.add(pokeball_for_smth)
            pokeballs_group.draw(new_screen)
        elif something.find("skill") != -1:
            skill = pygame.sprite.Sprite()
            skill_group = pygame.sprite.Group()
            skill_group.add((skill))
            skill.image = load_image("skill.png")
            skill.rect = skill.image.get_rect()
            skill.rect.x = 150
            skill.rect.y = 100
            string = font.render(something, False, pygame.Color('white'))
            rect = (150, 190, 25, 25)
            new_screen.blit(string, rect)
            skill_group.draw(new_screen)
        else:
            string = font.render(something, False, pygame.Color('white'))
            rect = (150, 120, 25, 25)
            new_screen.blit(string, rect)
    except:
        something_group = pygame.sprite.Group()
        something_group.add(something)
        something.set_rect(150, 150)
        something_group.draw(new_screen)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                new_screen.fill((0, 0, 0))
                return True
        pygame.display.flip()
        clock.tick(fps)


def terminate():
    pygame.quit()
    sys.exit()


fps = 60
start_screen()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill((0, 0, 0))
board = PyGameProjectSpriteMove.Board()
user = PyGameProjectSpriteMove.GameHero(16 * 9, 16 * 9)
camera = PyGameProjectSpriteMove.Camera(0, 0)
user_group.add(user)
board_group.add(board)
all_sprites.add(board, user)
running = True
while running:
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_5:
            menu(user, screen)
        something = user.update(board, event)
        if something:
            get_something(screen, something)
    camera.update(user)
    pygame.display.flip()
    for sprite in all_sprites:
        camera.apply(sprite)
    clock.tick(fps)
pygame.quit()