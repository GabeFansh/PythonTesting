import sys

import arcade
from src.constants import *
from src.attacks import *
import math
import os
import time
import random

attacked = False
items = False
mercy = False
act = False
current_health = STARTING_PLAYER_HEALTH


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


def menuCharacter(self, sprite, scale, xCoord, yCoord):
    self.menu_sprite = menuPlayer(sprite, scale)
    self.menu_sprite.center_x = xCoord
    self.menu_sprite.center_y = yCoord
    self.menu_list.append(self.menu_sprite)


def actCharacter(self, sprite, scale, xCoord, yCoord):
    self.act_sprite = menuPlayer(sprite, scale)
    self.act_sprite.center_x = xCoord
    self.act_sprite.center_y = yCoord
    self.act_list.append(self.act_sprite)


def enemySprite(self, sprite, scale, xCoord, yCoord):
    self.enemy_sprite = Enemy(sprite, scale)
    self.enemy_sprite.center_x = xCoord
    self.enemy_sprite.center_y = yCoord
    self.enemy_list.append(self.enemy_sprite)


def enemyBullet(self, sprite, scale, xCoord, yCoord, angle):
    self.bullet_sprite = EnemyBullet(sprite, scale)
    self.bullet_sprite.center_x = xCoord
    self.bullet_sprite.center_y = yCoord
    self.bullet_sprite.angle = math.degrees(angle)
    self.bullet_sprite.change_x = math.cos(angle) * BulletSpeed
    self.bullet_sprite.change_y = math.sin(angle) * BulletSpeed
    self.bullet_list.append(self.bullet_sprite)


def menuButton(centerX, centerY, text, textX, textY):
    arcade.draw_rectangle_outline(centerX,
                                  centerY,
                                  60,
                                  25,
                                  color=arcade.color.ORANGE)
    arcade.draw_text(text, textX, textY, color=arcade.color.ORANGE)


def actMenu(text, textX, textY):
    arcade.draw_text(text, textX, textY, color=arcade.color.WHITE, bold=True)


def playerHealth():
    arcade.draw_text("PLAYER", 20, 10, color=arcade.color.WHITE, bold=True)
    arcade.draw_text("LV 19", 95, 10, color=arcade.color.WHITE, bold=True)
    arcade.draw_xywh_rectangle_filled(150,
                                      10,
                                      STARTING_PLAYER_HEALTH,
                                      12,
                                      color=arcade.color.RED)
    arcade.draw_xywh_rectangle_filled(150,
                                      10, (current_health),
                                      12,
                                      color=arcade.color.YELLOW)
    arcade.draw_text(("{}/{}".format(current_health, STARTING_PLAYER_HEALTH)),
                     250,
                     10,
                     color=arcade.color.WHITE,
                     bold=True)


class Player(arcade.Sprite):
    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.angle += self.change_angle

        # Check for out-of-bounds
        if self.left < 50:
            self.left = 50
        elif self.right > 350:
            self.right = 350

        if self.bottom < 100:
            self.bottom = 100
        elif self.top > 225:
            self.top = 225


class Enemy(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right > SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class EnemyBullet(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class menuPlayer(arcade.Sprite):
    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds


class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)
        self.player_list = None
        self.player_sprite = None
        self.opponent_list = None
        self.opponent_sprite = None
        self.menu_list = None
        self.menu_sprite = None
        self.act_list = None
        self.act_sprite = None
        self.enemy_list = None
        self.enemy_sprite = None
        self.bullet_list = None
        self.bullet_sprite = None

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

        self.c_pressed = False
        self.x_pressed = False

        self.l_pressed = False

        self.q_pressed = False
        self.e_pressed = False

        self.frame_count = 0

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.opponent_list = arcade.SpriteList()
        self.menu_list = arcade.SpriteList()
        self.act_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        character(self, "blueHeart.png", 0.05, 150, 125)
        #opponentCharacter(self, "emoji.gif", 0.05, 150, 175)
        menuCharacter(self, "menuSelect.png", 0.05, 80, 40)
        actCharacter(self, "menuSelect.png", 0.05, 65, 207)
        enemySprite(self, "redHeart.png", 0.05, self.player_sprite.center_x,
                    300)
        enemySprite(self, "redHeart.png", 0.05,
                    (SCREEN_WIDTH - self.player_sprite.center_x), 50)

    def on_draw(self):
        global passed_fight_count
        arcade.start_render()

        if attacked == True:
            self.player_list.draw()
            #self.opponent_list.draw()
            self.enemy_list.draw()
            self.bullet_list.draw()

        if attacked == False and act == False and items == False:
            self.menu_list.draw()

        arcade.draw_lrtb_rectangle_outline(50,
                                           350,
                                           225,
                                           100,
                                           color=arcade.color.WHITE)

        if attacked == False and act == False and items == False:
            menuButton(80, 70, "FIGHT", 55, 65)
            menuButton(160, 70, "ACT", 143, 65)
            menuButton(240, 70, "ITEM", 220, 65)
            menuButton(320, 70, "MERCY", 292, 65)

        playerHealth()

        if act == True:
            self.act_list.draw()
            actMenu("Talk", 80, 200)
            actMenu("Shake", 80, 160)
            actMenu("Joke", 280, 200)
            actMenu("Insult", 280, 160)

        if items == True:
            self.act_list.draw()
            if item_one == True:
                actMenu(itemNames[0], itemCoords[5][0], itemCoords[5][1])
            if item_two == True:
                actMenu(itemNames[1], itemCoords[4][0], itemCoords[4][1])
            if item_three == True:
                actMenu(itemNames[2], itemCoords[3][0], itemCoords[3][1])
            if item_four == True:
                actMenu(itemNames[3], itemCoords[2][0], itemCoords[2][1])
            if item_five == True:
                actMenu(itemNames[4], itemCoords[1][0], itemCoords[1][1])
            if item_six == True:
                actMenu(itemNames[5], itemCoords[0][0], itemCoords[0][1])

        if passed_fight_count == 10:
            arcade.draw_xywh_rectangle_outline(0,
                                               0,
                                               SCREEN_WIDTH,
                                               SCREEN_HEIGHT,
                                               color=arcade.color.BLACK)
            arcade.draw_text("YOU WIN",
                             100,
                             200,
                             color=arcade.color.RED,
                             bold=True)
        if current_health == 0:
            arcade.draw_xywh_rectangle_outline(0,
                                               0,
                                               SCREEN_WIDTH,
                                               SCREEN_HEIGHT,
                                               color=arcade.color.BLACK)
            arcade.draw_text("YOU LOSE",
                             100,
                             200,
                             color=arcade.color.RED,
                             bold=True)

    def on_update(self, delta_time):
        global menu_choice
        global attacked
        global current_health
        global act
        global actVerticle_choice
        global actHorizontal_choice
        global items
        global itemVerticle_choice
        global itemHorizontal_choice

        global item_one
        global item_two
        global item_three
        global item_four
        global item_five
        global item_six
        global itemCoords
        global enemy_angle

        global passed_fight_count

        if passed_fight_count == 10:
            time.sleep(2)
            quit()
        if current_health == 0:
            time.sleep(2)
            quit()

        if attacked == True:
            self.frame_count += 1

            for enemy in self.enemy_list:
                startX = enemy.center_x
                startY = enemy.center_y

                dest1X = self.player_sprite.center_x
                dest1Y = self.player_sprite.center_y

                #dest2X = self.opponent_sprite.center_x
                #dest2Y = self.opponent_sprite.center_y

                x1Diff = dest1X - startX
                y1Diff = dest1Y - startY

                #x2Diff = dest2X - startX
                #y2Diff = dest2Y - startY

                enemy_angle = math.atan2(y1Diff, x1Diff)

                #if math.dist([startX, startY], [dest1X, dest2Y]) < math.dist([startX, startY], [dest2X, dest2Y]):
                #enemy_angle = math.atan2(y1Diff, x1Diff)
                #elif math.dist([startX, startY], [dest1X, dest2Y]) > math.dist([startX, startY], [dest2X, dest2Y]):
                #enemy_angle = math.atan2(y2Diff, x2Diff)

                enemy.angle = math.degrees(enemy_angle) - 90

                if self.frame_count % 30 == 0:
                    enemyBullet(self, "blueHeart.png", 0.05, startX, startY,
                                enemy_angle)
        for bullet in self.bullet_list:
            if bullet.top < 0 or bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()

        if attacked == False:
            for bullet in self.bullet_list:
                bullet.remove_from_sprite_lists()

        bullet_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.bullet_list)
        for bullet in bullet_hit_list:
            bullet.remove_from_sprite_lists()
            current_health -= 10

        if attacked == True:
            if self.frame_count % random.choice([400]) == 0:
                attacked = False
                passed_fight_count += 1

        for enemy in self.enemy_list:
            if self.frame_count % 100 == 0:
                enemy.center_x = random.randint(10, 390)
                if enemy.center_x < 20 or enemy.center_x > 380:
                    enemy.center_y = random.randint(50, 300)
                else:
                    enemy.center_y = random.choice([50, 300])

        if current_health > STARTING_PLAYER_HEALTH:
            current_health = STARTING_PLAYER_HEALTH
        elif current_health < 0:
            current_health = 0

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
        """self.opponent_sprite.change_x = 0
        self.opponent_sprite.change_y = 0

        if self.w_pressed and not self.s_pressed:
            self.opponent_sprite.change_y = MOVEMENT_SPEED
        elif self.s_pressed and not self.w_pressed:
            self.opponent_sprite.change_y = -MOVEMENT_SPEED
        if self.a_pressed and not self.d_pressed:
            self.opponent_sprite.change_x = -MOVEMENT_SPEED
        elif self.d_pressed and not self.a_pressed:
            self.opponent_sprite.change_x = MOVEMENT_SPEED

        self.opponent_list.update()"""

        self.menu_sprite.change_x = 0
        self.menu_sprite.change_y = 0

        if attacked == False and act == False and items == False:
            if self.left_pressed and not self.right_pressed:
                self.menu_sprite.change_x = -80
                self.left_pressed = False
                menu_choice -= 1
                if menu_choice < 1:
                    self.menu_sprite.change_x = 0
                    menu_choice = 1

            elif self.right_pressed and not self.left_pressed:
                self.menu_sprite.change_x = 80
                self.right_pressed = False
                menu_choice += 1

                if menu_choice > 4:
                    menu_choice = 4
                    self.menu_sprite.change_x = 0

            self.menu_list.update()

        self.act_sprite.change_x = 0
        self.act_sprite.change_y = 0

        if act == True:
            if itemVerticle_choice != 1 or itemHorizontal_choice != 1:
                itemVerticle_choice = 1
                itemHorizontal_choice = 1
                self.act_sprite.center_x = 65
                self.act_sprite.center_y = 207
                self.act_list.update()
            else:
                if self.up_pressed and not self.down_pressed:
                    self.act_sprite.change_y = 40
                    self.up_pressed = False
                    actVerticle_choice -= 1
                    if actVerticle_choice < 1:
                        self.act_sprite.change_y = 0
                        actVerticle_choice = 1

                elif self.down_pressed and not self.up_pressed:
                    self.act_sprite.change_y = -40
                    self.down_pressed = False
                    actVerticle_choice += 1
                    if actVerticle_choice > 2:
                        self.act_sprite.change_y = 0
                        actVerticle_choice = 2

                elif self.right_pressed and not self.left_pressed:
                    self.act_sprite.change_x = 200
                    self.right_pressed = False
                    actHorizontal_choice += 1
                    if actHorizontal_choice > 2:
                        self.act_sprite.change_x = 0
                        actHorizontal_choice = 2

                elif self.left_pressed and not self.right_pressed:
                    self.act_sprite.change_x = -200
                    self.left_pressed = False
                    actHorizontal_choice -= 1
                    if actHorizontal_choice < 1:
                        self.act_sprite.change_x = 0
                        actHorizontal_choice = 1

            self.act_list.update()

        if items == True:
            if actVerticle_choice != 1 or actHorizontal_choice != 1:
                actVerticle_choice = 1
                actHorizontal_choice = 1
                self.act_sprite.center_x = 65
                self.act_sprite.center_y = 207
                self.act_list.update()
            else:
                if self.up_pressed and not self.down_pressed:
                    self.act_sprite.change_y = 40
                    self.up_pressed = False
                    itemVerticle_choice -= 1
                    if itemVerticle_choice < 1:
                        self.act_sprite.change_y = 0
                        itemVerticle_choice = 1

                elif self.down_pressed and not self.up_pressed:
                    self.act_sprite.change_y = -40
                    self.down_pressed = False
                    itemVerticle_choice += 1
                    if itemVerticle_choice > 3:
                        self.act_sprite.change_y = 0
                        itemVerticle_choice = 3

                elif self.right_pressed and not self.left_pressed:
                    self.act_sprite.change_x = 200
                    self.right_pressed = False
                    itemHorizontal_choice += 1
                    if itemHorizontal_choice > 2:
                        self.act_sprite.change_x = 0
                        itemHorizontal_choice = 2

                elif self.left_pressed and not self.right_pressed:
                    self.act_sprite.change_x = -200
                    self.left_pressed = False
                    itemHorizontal_choice -= 1
                    if itemHorizontal_choice < 1:
                        self.act_sprite.change_x = 0
                        itemHorizontal_choice = 1

                if itemHorizontal_choice == 1:
                    if self.c_pressed == True:
                        self.c_pressed = False
                        if itemVerticle_choice == 1:
                            item_one = False
                            current_health = STARTING_PLAYER_HEALTH
                        elif itemVerticle_choice == 2:
                            item_two = False
                            current_health += 60
                        elif itemVerticle_choice == 3:
                            item_three = False
                            current_health += 50
                        items = False

                elif itemHorizontal_choice == 2:
                    if self.c_pressed == True:
                        self.c_pressed = False
                        if itemVerticle_choice == 1:
                            item_four = False
                        elif itemVerticle_choice == 2:
                            item_five = False
                        elif itemVerticle_choice == 3:
                            item_six = False
                        current_health += 20
                        items = False

            self.act_list.update()

        if menu_choice == 1:
            if self.c_pressed == True:
                self.c_pressed = False
                attacked = True
        elif menu_choice == 2:
            if self.c_pressed == True:
                self.c_pressed = False
                act = True
        elif menu_choice == 3:
            if self.c_pressed == True:
                self.c_pressed = False
                items = True

        if self.x_pressed == True:
            self.x_pressed = False
            attacked = False
            act = False
            items = False

        if self.l_pressed == True:
            self.l_pressed = False
            current_health -= 10
            if current_health < 0:
                current_health = 0

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

        if key == arcade.key.C:
            self.c_pressed = True
        elif key == arcade.key.X:
            self.x_pressed = True

        if key == arcade.key.L:
            self.l_pressed = True

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

        if key == arcade.key.C:
            self.c_pressed = False
        elif key == arcade.key.X:
            self.x_pressed = False

        if key == arcade.key.L:
            self.l_pressed = False


def main():
    """ Main function """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
