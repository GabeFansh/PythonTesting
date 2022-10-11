import arcade

menu_options = ["Pokedex", "Pokemon", "Bag", "Pokegear", "Red", "Save", "Options", "Debug", "Exit"]

def do_health(current):
    maxHealth = 100
    maxDashes = 10
    dashConvert = int(maxHealth / maxDashes)
    currentDashes = int(current / dashConvert)
    remainingHealth = maxDashes - currentDashes

    healthDisplay = '▮' * currentDashes
    remainingDisplay = ' ' * remainingHealth
    percent = str(int((current / maxHealth) * 100)) + "%"
    print("|" + healthDisplay + remainingDisplay + "|")
    print("    " + percent)
class PlayerMenu(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/PlayerMenu/PlayerMenu.png")
        self.scale = 0.4
        self.alpha = 0

        self.currentMenuOption = 0



    def MenuSelection(self, menuOption):
        print("Selected: " + menu_options[menuOption])
        if (menu_options[menuOption] == "Pokemon"):
            print("Rotom (Fire):")
            do_health(70)



class PlayerMenuSelect(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/PlayerMenu/PlayerMenuArrow.png")
        self.scale = 0.4
        self.alpha = 0
