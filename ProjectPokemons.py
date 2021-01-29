import pygame, os, sys, sqlite3


pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, image, x, y, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = self.load_image(image)

    def get_information_from_database(self, name):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM pokemons WHERE name={name}""").fetchall()
        evolution, skill = result[0], result[1]
        con.commit()
        return evolution, skill

    def change_information(self, name, skill, evolution):
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        cur.execute(f"""UPDATE pokemons SET skill={skill}, evolution={evolution} WHERE name={name}""")
        con.commit()

    def load_image(self, name, colorkey=None):
        fullname = os.path.join(name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image


class Bulbasaur(Pokemon):
    def __init__(self, x, y, *group):
        self.evolution, self.skill = self.get_information_from_database("Bulbasaur")
        if self.evolution == 1:
            name = "Bulbasauvr.png"
        if self.evolution == 2:
            name = "Ivysaur.png"
        if self.evolution == 3:
            name = "Venusaur.png"
        self.evvalue = 150
        super().__init__(f"{name}", x, y, *group)

    def update(self, addskill=0):
        self.skill += addskill
        if self.skill >= self.evvalue and self.evolution < 3:
            self.skill = 0
            self.evolution += 1
        self.change_information("Bulbasaur", self.skill, self.evolution)


class Charmander(Pokemon):
    def __init__(self, x, y, *group):
        self.evolution, self.skill = self.get_information_from_database("Charmander")
        if self.evolution == 1:
            name = "Charmander.png"
        if self.evolution == 2:
            name = "Charmeleon.png"
        if self.evolution == 3:
            name = "Charizard.png"
        self.evvalue = 250
        super().__init__(f"{name}", x, y, *group)

    def update(self, addskill=0):
        self.skill += addskill
        if self.skill >= self.evvalue and self.evolution < 3:
            self.skill = 0
            self.evolution += 1
        self.change_information("Charmander", self.skill, self.evolution)


class Squrtle(Pokemon):
    def __init__(self, x, y, *group):
        self.evolution, self.skill = self.get_information_from_database("Squrtle")
        if self.evolution == 1:
            name = "Squrtle.png"
        if self.evolution == 2:
            name = "Warturtle.png"
        self.evvalue = 350
        super().__init__(f"{name}", x, y, *group)

    def update(self, addskill=0):
        self.skill += addskill
        if self.skill >= self.evvalue and self.evolution < 2:
            self.skill = 0
            self.evolution += 1
        self.change_information("Squrtle", self.skill, self.evolution)


class Pikachu(Pokemon):
    def __init__(self, x, y, *group):
        self.evolution, self.skill = self.get_information_from_database("Pikachu")
        if self.evolution == 1:
            name = "Pikachu.png"
        if self.evolution == 2:
            name = "Raichu.png"
        self.evvalue = 450
        super().__init__(f"{name}", x, y, *group)

    def update(self, addskill=0):
        self.skill += addskill
        if self.skill >= self.evvalue and self.evolution < 2:
            self.skill = 0
            self.evolution += 1
        self.change_information("Pikachu", self.skill, self.evolution)


class Spearow(Pokemon):
    def __init__(self, x, y, *group):
        self.evolution, self.skill = self.get_information_from_database("Spearow")
        if self.evolution == 1:
            name = "Spearow.png"
        if self.evolution == 2:
            name = "Fearow.png"
        self.evvalue = 250
        super().__init__(f"{name}", x, y, *group)

    def update(self, addskill=0):
        self.skill += addskill
        if self.skill >= self.evvalue and self.evolution < 2:
            self.skill = 0
            self.evolution += 1
        self.change_information("Spearow", self.skill, self.evolution)