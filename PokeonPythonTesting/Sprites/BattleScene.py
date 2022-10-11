import arcade

menu_options = [["Fight", "Bag"], ["Pokemon", "Run"]]


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


class BattleScene(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(
            "C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/Battle/PokemonBattleBack.png")
        self.scale = 0.3
        self.alpha = 0


class BattleMenu(arcade.Sprite):


    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(
            "C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/Battle/BattleMenu.png")
        self.scale = 0.4
        self.alpha = 0
        self.h_option = 0
        self.v_option = 0




    def MenuSelection(self, top_bottom, left_right):
        print("Selected: " + menu_options[top_bottom][left_right])
        if menu_options[top_bottom][left_right] == "Pokemon":
            print("Rotom (Fire):")
            do_health(70)
            print()
            print(f"Bulbasaur:")
            do_health(80)

        if menu_options[top_bottom][left_right] == "Run":
            return 9


class BattleMenuSelect(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(
            "C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/Battle/BattleMenuArrow.png")
        self.scale = 0.75
        self.alpha = 0


class BattlePokemonFront(arcade.AnimatedTimeBasedSprite):
    def __init__(self):
        super().__init__()
        self.front_textures = []
        self.cur_texture = 0

        for i in range(99):
            self.front_textures.append(arcade.load_texture(
                "C:/Users/gfans/PycharmProjects/GameThing/Resources/Animated/Pokemon/Front/Bulbasaur.png", x=i * 96,
                y=0, width=96, height=96))
        self.scale = 1
        self.alpha = 0
        self.texture = self.front_textures[0]
        self.texture_change_frames = 30

    def update_animation(self, delta_time: float = 1 / 80):

        self.cur_texture += 1
        if self.cur_texture > 99:
            self.cur_texture = 0
        frame = self.cur_texture - 1
        self.texture = self.front_textures[frame]


class BattlePokemonBack(arcade.AnimatedTimeBasedSprite):
    def __init__(self):
        super().__init__()
        self.back_textures = []
        self.cur_texture = 0

        for i in range(60):
            self.back_textures.append(arcade.load_texture(
                "C:/Users/gfans/PycharmProjects/GameThing/Resources/Animated/Pokemon/Back/Rotom_Fire.png", x=i * 60, y=0,
                width=60, height=82))
        self.scale = 1
        self.alpha = 0
        self.texture = self.back_textures[0]
        self.texture_change_frames = 30

    def update_animation(self, delta_time: float = 1 / 80):

        self.cur_texture += 1
        if self.cur_texture > 60:
            self.cur_texture = 0
        frame = self.cur_texture - 1
        self.texture = self.back_textures[frame]


class TrainerPokemonHealth(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/Battle/PlayerHealth.png")
        self.alpha = 0


class OpponentPokemonHealth(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("C:/Users/gfans/PycharmProjects/GameThing/Resources/Still/Battle/OpponentHealth.png")
        self.alpha = 0

