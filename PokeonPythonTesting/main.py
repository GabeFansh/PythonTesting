"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""

import arcade
import random
from Sprites.Player import *
from Sprites.Grass import *
from Sprites.PlayerMenu import *
from Sprites.BattleScene import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 5
CHARACTER_SCALING = 2


class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """


    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = None
        self.player = None
        self.grass_list = None
        self.grass = None
        self.playermenu_list = None
        self.playermenu = None
        self.playermenuselector = None
        self.battleScene_list = None
        self.battleScene = None


        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        self.player_list = arcade.SpriteList()
        self.player = Player()

        self.battleScene_list = arcade.SpriteList()
        self.shape_list = []

        self.battleScene = BattleScene()
        self.battleScene.right = SCREEN_WIDTH
        self.battleScene.top = SCREEN_HEIGHT
        self.battleScene_list.append(self.battleScene)

        self.battleScene = BattleMenu()
        self.battleScene.top = self.battleScene_list[0].bottom
        self.battleScene.left = self.battleScene_list[0].left
        self.battleScene_list.append(self.battleScene)

        self.battleScene = BattleMenuSelect()
        self.battleScene.top = self.battleScene_list[0].bottom - 25
        self.battleScene.left = self.battleScene_list[0].left + 15
        self.battleScene_list.append(self.battleScene)

        self.battleScene = BattlePokemonFront()
        self.battleScene.center_x = SCREEN_WIDTH - 100
        self.battleScene.center_y = SCREEN_HEIGHT - 75
        self.battleScene_list.append(self.battleScene)

        self.battleScene = BattlePokemonBack()
        self.battleScene.center_x = SCREEN_WIDTH - 225
        self.battleScene.center_y = SCREEN_HEIGHT - 100
        self.battleScene_list.append(self.battleScene)

        self.battleScene = TrainerPokemonHealth()
        self.battleScene.right = self.battleScene_list[0].right
        self.battleScene.center_y = self.battleScene_list[0].bottom + 20
        self.battleScene_list.append(self.battleScene)

        self.battleScene = OpponentPokemonHealth()
        self.battleScene.left = self.battleScene_list[0].left
        self.battleScene.center_y = self.battleScene_list[0].top - 20
        self.battleScene_list.append(self.battleScene)

        self.grass_list = arcade.SpriteList()
        self.playermenu_list = arcade.SpriteList()

        self.player.center_x = SCREEN_WIDTH / 2
        self.player.center_y = SCREEN_HEIGHT / 2
        self.player_list.append(self.player)

        self.playermenu = PlayerMenu()
        self.playermenu.center_x = SCREEN_WIDTH / 2
        self.playermenu.center_y = SCREEN_HEIGHT / 2
        self.playermenu_list.append(self.playermenu)


        self.playermenuselector = PlayerMenuSelect()
        self.playermenuselector.center_x = self.playermenu.center_x - 30
        self.playermenuselector.center_y = self.playermenu.center_y + 64
        self.playermenu_list.append(self.playermenuselector)






        for r in range(0,10):
            for c in range(0,10):
                self.grass = Grass()
                self.grass.center_y = self.grass.center_y + (r*25)
                self.grass.center_x = self.grass.center_x + (c*25)
                self.grass_list.append(self.grass)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        self.grass_list.draw()
        self.playermenu_list.draw()
        self.player_list.draw()
        self.battleScene_list.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """



        self.player_list.update()

        # Update the players animation
        self.player_list.update_animation()
        self.battleScene_list.update_animation()
        self.playermenu_list.update()

        if self.player.left < 0:
            self.player.left = 0
        elif self.player.right > SCREEN_WIDTH - 1:
            self.player.right = SCREEN_WIDTH - 1

        if self.player.bottom < 0:
            self.player.bottom = 0
        elif self.player.top > SCREEN_HEIGHT - 1:
            self.player.top = SCREEN_HEIGHT - 1

        if abs(self.player.center_x - SCREEN_WIDTH) > abs(self.player.center_x + 0):
            self.playermenu.center_x = self.player.center_x + 50
        elif abs(self.player.center_x - SCREEN_WIDTH) < abs(self.player.center_x + 0):
            self.playermenu.center_x = self.player.center_x - 50

        if abs(self.player.center_y - SCREEN_HEIGHT) > abs(self.player.center_y + 0):
            self.playermenu.center_y = self.player.center_y + 50
        elif abs(self.player.center_y - SCREEN_HEIGHT) < abs(self.player.center_y + 0):
            self.playermenu.center_y = self.player.center_y - 50


        colliding = arcade.check_for_collision_with_list(self.player, self.grass_list)
        if (abs(self.player.change_x) > 0 or abs(self.player.change_y) > 0) and (len(colliding) > 0):
            encounter = random.randint(1,100)
            if encounter == 3:
                for each in self.battleScene_list:
                    each.alpha = 255

    def on_key_press(self, key, key_modifiers):



        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if self.playermenu.alpha == 0 and self.battleScene_list[0].alpha == 0:
            if key == arcade.key.UP:
                self.player.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.player.change_y = -MOVEMENT_SPEED
            elif key == arcade.key.LEFT:
                self.player.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.player.change_x = MOVEMENT_SPEED

        if self.playermenu.alpha == 255:
            self.player.change_y = 0
            self.player.change_x = 0
            if key == arcade.key.DOWN:
                if self.playermenu.currentMenuOption == 8:
                    pass
                else:
                    self.playermenuselector.center_y = self.playermenuselector.center_y - 16
                    self.playermenu.currentMenuOption += 1
            if key == arcade.key.UP:
                if self.playermenu.currentMenuOption == 0:
                    pass
                else:
                    self.playermenuselector.center_y = self.playermenuselector.center_y + 16
                    self.playermenu.currentMenuOption -= 1
            if key == arcade.key.X:
                PlayerMenu.MenuSelection(self, self.playermenu.currentMenuOption)


        if self.battleScene_list[0].alpha == 0:
            if key == arcade.key.C:
                self.playermenuselector.center_x = self.playermenu.center_x - 30
                self.playermenuselector.center_y = self.playermenu.center_y + 64
                self.player.change_x = 0
                self.player.change_y = 0
                if self.playermenu.alpha == 0:
                    self.playermenu.alpha = 255
                    self.playermenuselector.alpha = 255
                elif self.playermenu.alpha == 255:
                    self.playermenu.alpha = 0
                    self.playermenuselector.alpha = 0

        if self.battleScene_list[0].alpha == 255:
            self.player.change_y = 0
            self.player.change_x = 0
            if key == arcade.key.DOWN:
                if self.battleScene_list[1].v_option == 1:
                    pass
                else:
                    self.battleScene_list[2].center_y = self.battleScene_list[2].center_y - 32
                    self.battleScene_list[1].v_option += 1
            if key == arcade.key.UP:
                if self.battleScene_list[1].v_option == 0:
                    pass
                else:
                    self.battleScene_list[2].center_y = self.battleScene_list[2].center_y + 32
                    self.battleScene_list[1].v_option -= 1
            if key == arcade.key.RIGHT:
                if self.battleScene_list[1].h_option == 1:
                    pass
                else:
                    self.battleScene_list[2].center_x = self.battleScene_list[2].center_x + 110
                    self.battleScene_list[1].h_option += 1
            if key == arcade.key.LEFT:
                if self.battleScene_list[1].h_option == 0:
                    pass
                else:
                    self.battleScene_list[2].center_x = self.battleScene_list[2].center_x - 110
                    self.battleScene_list[1].h_option -= 1
            if key == arcade.key.X:
                if BattleMenu.MenuSelection(self, self.battleScene_list[1].v_option, self.battleScene_list[1].h_option) == 9:
                    for each in self.battleScene_list:
                        each.alpha = 0






    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

        if key == arcade.key.C:
            self.playermenu.currentMenuOption = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()