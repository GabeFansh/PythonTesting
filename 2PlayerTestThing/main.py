import arcade
from src.constants import *
import math
import os


def character(self, sprite, scale, xCoord, yCoord):
    self.player_sprite = Player(sprite, scale)
    self.player_sprite.center_x = xCoord
    self.player_sprite.center_y = yCoord
    self.player_list.append(self.player_sprite)


def opponentCharacter(self, sprite, scale, xCoord, yCoord):
    self.opponent_sprite = Player(sprite, scale)
    self.opponent_sprite.center_x = xCoord
    self.opponent_sprite.center_y = yCoord
    self.opponent_list.append(self.opponent_sprite)


class Player(arcade.Sprite):
    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)
        self.player_list = None
        self.player_sprite = None
        self.opponent_list = None
        self.opponent_sprite = None
        self.player_physics_engine = None
        self.opponent_physics_engine = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        self.w_pressed = False
        self.a_pressed = False
        self.s_pressed = False
        self.d_pressed = False

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.opponent_list = arcade.SpriteList()
        character(self, "blueHeart.png", 0.05, 100, 200)
        opponentCharacter(self, "redHeart.png", 0.05, 300, 200)

        self.player_physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.opponent_list)
        self.opponent_physics_engine = arcade.PhysicsEngineSimple(
            self.opponent_sprite, self.player_list)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.opponent_list.draw()

    def on_update(self, delta_time):
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        self.player_list.update()

        self.opponent_sprite.change_x = 0
        self.opponent_sprite.change_y = 0

        if self.w_pressed and not self.s_pressed:
            self.opponent_sprite.change_y = MOVEMENT_SPEED
        elif self.s_pressed and not self.w_pressed:
            self.opponent_sprite.change_y = -MOVEMENT_SPEED
        if self.a_pressed and not self.d_pressed:
            self.opponent_sprite.change_x = -MOVEMENT_SPEED
        elif self.d_pressed and not self.a_pressed:
            self.opponent_sprite.change_x = MOVEMENT_SPEED



        self.opponent_list.update()

        self.player_physics_engine.update()
        self.opponent_physics_engine.update()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        if key == arcade.key.W:
            self.w_pressed = True
        elif key == arcade.key.S:
            self.s_pressed = True
        elif key == arcade.key.A:
            self.a_pressed = True
        elif key == arcade.key.D:
            self.d_pressed = True

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

        if key == arcade.key.W:
            self.w_pressed = False
        elif key == arcade.key.S:
            self.s_pressed = False
        elif key == arcade.key.A:
            self.a_pressed = False
        elif key == arcade.key.D:
            self.d_pressed = False


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
