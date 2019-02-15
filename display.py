#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pygame as pg


class Display:
    SPRITE_SIZE = 30
    SPRITE_N = 15
    BOARD_SIZE = SPRITE_SIZE * SPRITE_N

    def __init__(self):
        pg.init()
        pg.display.set_caption("Help Mac Gyver to escape!")
        pg.key.set_repeat(400, 30)

        self.window = pg.display.set_mode((self.BOARD_SIZE, self.BOARD_SIZE))
        self.image = {"ground": pg.image.load("ressources/sol.png").convert(),
                      "wall": pg.image.load("ressources/wall.png").convert(),
                      "guardian": pg.image.load("ressources/Gardien.png").convert(),
                      "item_one": pg.image.load("ressources/ether.png").convert(),
                      "item_two": pg.image.load("ressources/seringue.png").convert(),
                      "item_three": pg.image.load("ressources/aiguille.png").convert()}

        self.text_load = pg.font.SysFont("cosmicsansms", 32)
        self.msg_load = self.text_load.render("To play, press ENTER or Q for quit", True, (255, 255, 255))
        self.msg_final = self.text_load.render("Great!! You are free!", True, (255, 255, 255))
        self.msg_dead = self.text_load.render("You are dead!", True, (255, 255, 255))

    def display_map(self, map):
        """ Show map """

        for y, line in enumerate(map):
            for x, sprite in enumerate(line):
                y_sprite = y * 30
                x_sprite = x * 30
                if sprite == "#":
                    self.window.blit(self.image["wall"], (x_sprite, y_sprite))
                elif sprite == "G":
                    self.window.blit(self.image["guardian"], (x_sprite, y_sprite))
                elif sprite == " ":
                    self.window.blit(self.image["ground"], (x_sprite, y_sprite))
                elif sprite == "1":
                    self.window.blit(self.image["item_one"], (x_sprite, y_sprite))
                elif sprite == "2":
                    self.window.blit(self.image["item_two"], (x_sprite, y_sprite))
                elif sprite == "3":
                    self.window.blit(self.image["item_three"], (x_sprite, y_sprite))

    def mac_gyver(self, y, x):
        macgyver = pg.image.load("ressources/MacGyver.png").convert()
        self.window.blit(macgyver, ((x * 30), (y * 30)))

    def message(self, msg):
        self.window.blit(msg, (150, 190))

    def counter(self, total_items):
        counter = self.text_load.render("Items: " + str(total_items), True, (255, 255, 255))
        self.window.blit(counter, (360, 4))
