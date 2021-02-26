if __name__ == "main":
    pass

else:
    import pygame, os, sys


    class Pokemon(pygame.sprite.Sprite):
        def __init__(self, images, *group):
            super().__init__(*group)
            self.images = []
            for e in images:
                self.images.append(self.load_image(e))

        def get_information_from_database(self, name):
            try:
                file = open(f"Data/Pokemon_{name}.txt", mode="r")
                evolution = int(file.read(1))
                skill = int(file.read())
                file.close()
                return evolution, skill
            except:
                file = open(f"Data/Pokemon_{name}.txt", mode="w")
                file.write("1")
                file.write("0")
                file.close()
                return 1, 0

        def change_information(self, name, skill, evolution):
            file = open(f"Data/Pokemon_{name}.txt", mode="w")
            file.write(str(evolution))
            file.write(str(skill))
            file.close()

        def change_image(self):
            self.image = self.images[self.evolution - 1]
            self.rect = self.image.get_rect()

        def load_image(self, name, colorkey=None):
            fullname = os.path.join(f"Data/{name}")
            if not os.path.isfile(fullname):
                print(f"Файл с изображением '{fullname}' не найден")
                sys.exit()
            image = pygame.image.load(fullname)
            return image

        def set_rect(self, x, y):
            self.rect.x = x
            self.rect.y = y

        def get_information(self):
            return self.evolution, self.skill

        def name_pokemon(self):
            return self.name


    class Bulbasaur(Pokemon):
        def __init__(self, x, y, *group):
            self.evolution, self.skill = self.get_information_from_database("Bulbasaur")
            self.evvalue = 150
            super().__init__(["Bulbasauvr.png", "Venusaur.png", "Ivysaur.png"], *group)
            self.name = "bulbasauvr"
            self.image = self.images[self.evolution - 1]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.update()

        def update(self, addskill=0):
            self.skill += addskill
            if self.skill >= self.evvalue and self.evolution < 3:
                self.skill = 0
                self.evolution += 1
                self.change_image()
            self.change_information("Bulbasaur", self.skill, self.evolution)


    class Charmander(Pokemon):
        def __init__(self, x, y, *group):
            self.evolution, self.skill = self.get_information_from_database("Charmander")
            self.evvalue = 250
            super().__init__(["Charmander.png", "Charmeleon.png", "Charizard.png"], *group)
            self.name = "charmander"
            self.image = self.images[self.evolution - 1]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.update()

        def update(self, addskill=0):
            self.skill += addskill
            if self.skill >= self.evvalue and self.evolution < 3:
                self.skill = 0
                self.evolution += 1
                self.change_image()
            self.change_information("Charmander", self.skill, self.evolution)


    class Squrtle(Pokemon):
        def __init__(self, x, y, *group):
            self.evolution, self.skill = self.get_information_from_database("Squrtle")
            self.evvalue = 350
            super().__init__(["Squrtle.png", "Warturtle.png"], *group)
            self.name = "squrtle"
            self.image = self.images[self.evolution - 1]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.update()

        def update(self, addskill=0):
            self.skill += addskill
            if self.skill >= self.evvalue and self.evolution < 2:
                self.skill = 0
                self.evolution += 1
                self.change_image()
            self.change_information("Squrtle", self.skill, self.evolution)


    class Pikachu(Pokemon):
        def __init__(self, x, y, *group):
            self.evolution, self.skill = self.get_information_from_database("Pikachu")
            self.evvalue = 450
            super().__init__(["Pikachu.png", "Raichu.png"], *group)
            self.name = "pikachu"
            self.image = self.images[self.evolution - 1]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.update()

        def update(self, addskill=0):
            self.skill += addskill
            if self.skill >= self.evvalue and self.evolution < 2:
                self.skill = 0
                self.evolution += 1
                self.change_image()
            self.change_information("Pikachu", self.skill, self.evolution)


    class Spearow(Pokemon):
        def __init__(self, x, y, *group):
            self.evolution, self.skill = self.get_information_from_database("Spearow")
            self.evvalue = 250
            super().__init__(["Spearow.png", "Fearow.png"], group)
            self.name = "spearow"
            self.image = self.images[self.evolution - 1]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.update()

        def update(self, addskill=0):
            self.skill += addskill
            if self.skill >= self.evvalue and self.evolution < 2:
                self.skill = 0
                self.evolution += 1
                self.change_image()

            self.change_information("Spearow", self.skill, self.evolution)