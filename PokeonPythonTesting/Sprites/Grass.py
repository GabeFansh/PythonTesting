import arcade
import random

class Grass(arcade.Sprite):


    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/Grass/Grass.png")
        self.scale = 0.80
        self.center_x = 50
        self.center_y = 50
        self.wild_pokemon = False


    def PlayerOnGrass(self, collision):
        if len(collision) > 0:
            self.wild_pokemon = True;
        else:
            self.wild_pokemon = False
        if self.wild_pokemon == True:
            encounter = random.randint(1,100)
            if encounter == 3:
                return 1

