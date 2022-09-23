import arcade

menu_options = ["Pokedex", "Pokemon", "Bag", "Pokegear", "Red", "Save", "Options", "Debug", "Exit"]


class PlayerMenu(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/PlayerMenu/PlayerMenu.png")
        self.scale = 0.4
        self.alpha = 0

        self.currentMenuOption = 0



    def MenuSelection(self, menuOption):
        print("Selected: " + menu_options[menuOption])


class PlayerMenuSelect(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/PlayerMenu/PlayerMenuArrow.png")
        self.scale = 0.4
        self.alpha = 0
