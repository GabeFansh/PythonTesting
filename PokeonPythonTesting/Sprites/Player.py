import arcade



class Player(arcade.Sprite):


    DIRECTIONS = ["Down","Left","Right","Up"]

    def __init__(self):
        super().__init__()
        self.name = ""
        self.health = 100
        self.shield = 25
        self.RIGHT_DIRECTION = 0
        self.LEFT_DIRECTION = 1
        self.UP_DIRECTION = 2
        self.DOWN_DIRECTION = 3
        self.character_face_direction = 2
        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]
        self.cur_texture = 0
        self.scale = 1

        main_path = "C:/Users/gfans/PycharmProjects/GameThing/Resources/Animated/MainPlayer"

        self.idle_texture_pair = arcade.load_texture(f"{main_path}/tile0.png")


        self.right_textures = []
        self.up_textures = []
        self.down_textures = []
        self.left_textures = []

        for i in range(0, 4):
            self.down_textures.append(arcade.load_texture(f"{main_path}/tile{i}.png"))
        for i in range(4, 8):
            self.left_textures.append(arcade.load_texture(f"{main_path}/tile{i}.png"))
        for i in range(8, 12):
            self.right_textures.append(arcade.load_texture(f"{main_path}/tile{i}.png"))
        for i in range(12, 16):
            self.up_textures.append(arcade.load_texture(f"{main_path}/tile{i}.png"))




    def update_animation(self, delta_time: float = 1 / 30):
        if self.change_x < 0:# and self.character_face_direction == self.RIGHT_DIRECTION:
            self.character_face_direction = 1
        elif self.change_x > 0:# and self.character_face_direction == self.LEFT_DIRECTION:
            self.character_face_direction = 0
        elif self.change_y < 0:# and self.character_face_direction == self.UP_DIRECTION:
            self.character_face_direction = 3
        elif self.change_y > 0:# and self.character_face_direction == self.DOWN_DIRECTION:
            self.character_face_direction = 2

        if self.change_x == 0 and self.change_y == 0:
            if self.character_face_direction == self.UP_DIRECTION:
                self.texture = self.up_textures[0]
            elif self.character_face_direction == self.DOWN_DIRECTION:
                self.texture = self.down_textures[0]
            elif self.character_face_direction == self.LEFT_DIRECTION:
                self.texture = self.left_textures[0]
            elif self.character_face_direction == self.RIGHT_DIRECTION:
                self.texture = self.right_textures[0]
            return

        self.cur_texture += 1
        if self.cur_texture > 8:
            self.cur_texture = 0
        frame = (self.cur_texture % 4) - 1
        player_direction = self.character_face_direction
        if player_direction == self.UP_DIRECTION:
            self.texture = self.up_textures[frame]
        elif player_direction == self.DOWN_DIRECTION:
            self.texture = self.down_textures[frame]
        elif player_direction == self.LEFT_DIRECTION:
            self.texture = self.left_textures[frame]
        elif player_direction == self.RIGHT_DIRECTION:
            self.texture = self.right_textures[frame]


