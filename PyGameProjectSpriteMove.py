if __name__ == "main":
    pass
else:
    import pygame, os, sys
    import PyGameProjectPokemons
    from Board import BOARD, BOARD_SIZE, CELL_SIZE, POKEMON_CHANCE, BOOST_CHANCE, POKEBALL_CHANCE
    from random import choice

    pygame.init()
    user_group = pygame.sprite.Group()
    board_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    pokemons_group = pygame.sprite.Group()


    class GameHero(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__(user_group, all_sprites)
            self.image_list = []
            self.image_list.append(self.load_image("Hero_Front.png"))
            self.image_list.append(self.load_image("Hero_Back.png"))
            self.image_list.append(self.load_image("Hero_Left.png"))
            self.image_list.append(self.load_image("Hero_Right.png"))
            self.image_list.append(self.load_image("HeroGo.png"))
            self.image_list.append(self.load_image("HeroGoLeft.png"))
            self.image = self.load_image("Hero_Front.png")
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.start_x = x
            self.start_y = y
            self.rect.y = y
            self.pokemons = []
            self.pokeballs = 0
            self.get_information()

        def get_information(self):
            try:
                file = open("Data/pokemons.txt", mode="r")
                data = file.readlines()
                for e in data:
                    e = e.split("\n")[0]
                    if e == "spearow":
                        self.pokemons.append(PyGameProjectPokemons.Spearow(0, 0))
                        self.pokemons[-1].update()
                    if e == "pikachu":
                        self.pokemons.append(PyGameProjectPokemons.Pikachu(0, 0))
                    if e == "squrtle":
                        self.pokemons.append(PyGameProjectPokemons.Squrtle(0, 0))
                    if e == "charmander":
                        self.pokemons.append(PyGameProjectPokemons.Charmander(0, 0))
                    if e == "bulbasauvr":
                        self.pokemons.append(PyGameProjectPokemons.Bulbasaur(0, 0))
                file.close()
            except:
                file = open("Data/pokemons.txt", mode="w")
                file.close()

        def change_information(self, pokemon):
            file = open("Data/pokemons.txt", mode="r")
            data = file.read()
            file.close()
            if pokemon in data.split("\n"):
                return 1
            else:
                file = open("Data/pokemons.txt", mode="a")
                file.write(f"\n{pokemon}")
                file.close()
                return 0

        def get_pokeballs(self):
            return self.pokeballs

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
            fullname = os.path.join(f"Data/{name}")
            if not os.path.isfile(fullname):
                print(f"Файл с изображением '{fullname}' не найден")
                sys.exit()
            image = pygame.image.load(fullname)
            return image

        def update(self, target, *args):
            if args and args[0].type == pygame.KEYDOWN:
                if args[0].key == pygame.K_UP:
                    self.image = self.turn_back()
                    if target.click(self.rect.x, self.rect.y - 16) == 2:
                        self.rect = self.rect.move(0, -16)
                    if target.click(self.rect.x, self.rect.y - 16) == 1:
                        return self.choose_something()

                if args[0].key == pygame.K_LEFT:
                    self.image = self.turn_left()
                    if target.click(self.rect.x - 16, self.rect.y) == 2:
                        self.rect = self.rect.move(- 16, 0)
                    if target.click(self.rect.x - 16, self.rect.y) == 1:
                        return self.choose_something()

                if args[0].key == pygame.K_DOWN:
                    self.image = self.turn_forward()
                    if target.click(self.rect.x, self.rect.y + 16) == 2:
                        self.rect = self.rect.move(0, 16)
                    if target.click(self.rect.x, self.rect.y + 16) == 1:
                        return self.choose_something()

                if args[0].key == pygame.K_RIGHT:
                    self.image = self.turn_right()
                    if target.click(self.rect.x + 16, self.rect.y) == 2:
                        self.rect = self.rect.move(16, 0)
                    if target.click(self.rect.x + 16, self.rect.y) == 1:
                        return self.choose_something()
            return None

        def choose_something(self):
            seq = [0] * (100 - POKEMON_CHANCE - POKEBALL_CHANCE - BOOST_CHANCE) + \
                  [1] * POKEMON_CHANCE + [2] * BOOST_CHANCE + [3] * POKEBALL_CHANCE
            c = choice(seq)
            if c == 0:
                return None
            if c == 1 and self.pokeballs > 0:
                return self.choose_pokemon()
            if c == 1 and self.pokeballs == 0:
                return "here may be pokemon, but it run away, because you haven't pokeball"
            if c == 2 and self.pokemons:
                skill = choice([10, 10, 20, 10, 20, 30, 10, 50])
                e = choice(self.pokemons)
                self.append_skill(e, skill)
                return f"skill: {skill} for pokemon {e.name_pokemon()}!"
            if c == 3:
                self.append_pokeball()
                return "pokeball"

        def choose_pokemon(self):
            c = choice([1, 2, 3, 4, 5])
            if c == 1:
                if self.change_information("bulbasauvr"):
                    for e in self.pokemons:
                        if e.name_pokemon() == "bulbasauvr":
                            self.append_skill(e, 30)
                            return "You have this pokemon, your pokemon get +30"
                self.pokemons.append(PyGameProjectPokemons
                                     .Bulbasaur(self.rect.x, self.rect.y, pokemons_group, all_sprites))
            if c == 2:
                if self.change_information("charmander"):
                    for e in self.pokemons:
                        if e.name_pokemon() == "charmander":
                            self.append_skill(e, 30)
                            return "You have this pokemon, your pokemon get +30"
                self.pokemons.append(PyGameProjectPokemons
                                     .Charmander(self.rect.x, self.rect.y, pokemons_group, all_sprites))
            if c == 3:
                if self.change_information("squrtle"):
                    for e in self.pokemons:
                        if e.name_pokemon() == "squrtle":
                            self.append_skill(e, 30)
                            return "You have this pokemon, your pokemon get +30"
                self.pokemons.append(PyGameProjectPokemons
                                     .Squrtle(self.rect.x, self.rect.y, pokemons_group, all_sprites))
            if c == 4:
                if self.change_information("pikachu"):
                    for e in self.pokemons:
                        if e.name_pokemon() == "pikachu":
                            self.append_skill(e, 30)
                    return "You have this pokemon, your pokemon get +30"
                self.pokemons.append(PyGameProjectPokemons
                                     .Pikachu(self.rect.x, self.rect.y, pokemons_group, all_sprites))
            if c == 5:
                if self.change_information("spearow"):
                    for e in self.pokemons:
                        if e.name_pokemon() == "spearow":
                            self.append_skill(e, 30)
                    return "You have this pokemon, your pokemon get +30"
                self.pokemons.append(PyGameProjectPokemons
                                     .Spearow(self.rect.x, self.rect.y, pokemons_group, all_sprites))
            self.pokeballs -= 1
            return self.pokemons[-1]

        def append_skill(self, pokemon, skill):
            pokemon.update(addskill=skill)

        def append_pokeball(self):
            self.pokeballs += 1

        def start_posx(self):
            return self.start_x

        def start_posy(self):
            return self.start_y

        def get_pokemons(self):
            return self.pokemons


    class Board(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__(board_group, all_sprites)
            self.image = self.load_image("map.png")
            self.rect = self.image.get_rect()

        def load_image(self, name, colorkey=None):
            fullname = os.path.join(f"Data/{name}")
            if not os.path.isfile(fullname):
                print(f"Файл с изображением '{fullname}' не найден")
                sys.exit()
            image = pygame.image.load(fullname)
            return image

        def click(self, pos_x, pos_y):
            if pos_y > BOARD_SIZE[1] * CELL_SIZE[1] + self.rect.y or \
                    pos_x > BOARD_SIZE[0] * CELL_SIZE[0] + self.rect.x or pos_x < self.rect.x or \
                    pos_y < self.rect.y:
                return -1
            x = (pos_x - self.rect.x) // CELL_SIZE[0]
            y = (pos_y - self.rect.y) // CELL_SIZE[1]
            return self.can_move(x, y)

        def can_move(self, x, y):
            if BOARD[y][x] in ["water", "tree", "cocostree", "well", "rock"]:
                return 1
            if BOARD[y][x] in ["store", "house"]:
                return 0
            return 2


    class Camera:
        # зададим начальный сдвиг камеры
        def __init__(self, x, y):
            self.dx = 0
            self.dy = 0
            self.pole_width = x
            self.pole_height = y

        def apply(self, obj):
            obj.rect.x = obj.rect.x + self.dx
            obj.rect.y = obj.rect.y + self.dy

        # позиционировать камеру на объекте target
        def update(self, target):
            self.dx = -(target.rect.x - target.start_posx())
            self.dy = -(target.rect.y - target.start_posy())