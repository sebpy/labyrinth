#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Display class """

import pygame as pg


class Display:
    """ show interface graphic with pygame """
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
                      "item_three": pg.image.load("ressources/aiguille.png").convert(),
                      "mac_gyver": pg.image.load("ressources/MacGyver.png").convert()}

        self.text_load = pg.font.SysFont("cosmicsansms", 32)
        self.msg_load = self.text_load.render("To play, press ENTER or Q for quit",
                                              True, (255, 255, 255))
        self.msg_free = self.text_load.render("Great!! You are free!", True, (255, 255, 255))
        self.msg_dead = self.text_load.render("You are dead!", True, (255, 255, 255))

    def display_map(self, mapping):
        """ Show map """

        for y_pos, line in enumerate(mapping):
            for x_pos, sprite in enumerate(line):
                y_sprite = y_pos * 30
                x_sprite = x_pos * 30
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

    def counter(self, items):
        """ Show items counter """
        counter_items = self.text_load.render("Items: " + str(items), True, (255, 255, 255))
        i = 12
        while i < 15:
            self.window.blit(self.image["wall"], ((i * 30), (0 * 30)))
            i += 1

        self.window.blit(counter_items, (360, 4))

    def mac_gyver(self, y_pos, x_pos):
        """ Create Mac Gyver sprite """
        self.window.blit(self.image["mac_gyver"], ((x_pos * 30), (y_pos * 30)))

    def message(self, msg):
        """ Print messages on screen """
        if msg == self.msg_free:
            self.window.blit(msg, (140, 220))
        elif msg == self.msg_dead:
            self.window.blit(msg, (160, 220))

    def display_flip(self):
        """ display pygame """
        pg.display.flip()

    def clean_box(self, y_pos, x_pos):
        """ change old position of MG by ground sprite """
        self.window.blit(self.image["ground"], ((x_pos * 30), (y_pos * 30)))
