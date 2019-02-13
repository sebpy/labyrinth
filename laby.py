#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Class labyrinth with all methods """

import random as rd
import pygame

class Labyrinth:
    """ Create labyrinth with wall.txt """

    def __init__(self):
        self.start_game = 0
        self.map = []  # variable map with list
        self.total_items = 0  # initialize variable total_items
        self.pos_x = 0
        self.pos_y = 1

    def load_map(self):
        """ Open wall.txt file with structure of labyrinth """

        with open('wall.txt', 'r') as laby:  # open wall.txt
            for line in laby:
                i = []  # create l list
                for char in line:
                    if char != "\n":  # del last \n
                        i.append(char)
                self.map.append(i)

    def randomize_items(self):
        """ Place 3 items in labyrinth """

        i = ["1", "2", "3"]
        while i:
            pos_y = rd.randint(0, 14)  # generates a number between 0 and the number of rows
            pos_x = rd.randint(0, 14)  # generates a number between 0 and the number of col
            if self.map[pos_y][pos_x] == " ":
                self.map[pos_y][pos_x] = i[0]
                i.pop(0)

    def display_map(self, window):
        """ Show map """

        ground = pygame.image.load("ressources/sol.png").convert()
        wall = pygame.image.load("ressources/wall.png").convert()
        guardian = pygame.image.load("ressources/Gardien.png").convert()
        item_one = pygame.image.load("ressources/ether.png").convert()
        item_two = pygame.image.load("ressources/seringue.png").convert()
        item_three = pygame.image.load("ressources/aiguille.png").convert()

        line_n = 0
        for line in self.map:
            rows_n = 0
            for sprite in line:
                y_sprite = line_n * 30
                x_sprite = rows_n * 30
                if sprite == "#":
                    window.blit(wall, (x_sprite, y_sprite))
                elif sprite == "G":
                    window.blit(guardian, (x_sprite, y_sprite))
                elif sprite == " ":
                    window.blit(ground, (x_sprite, y_sprite))
                elif sprite == "1":
                    window.blit(item_one, (x_sprite, y_sprite))
                elif sprite == "2":
                    window.blit(item_two, (x_sprite, y_sprite))
                elif sprite == "3":
                    window.blit(item_three, (x_sprite, y_sprite))
                rows_n += 1
            line_n += 1

    def guardian(self, pos_y, pos_x):
        """ Return Position of guardian """
        return self.map[pos_y][pos_x] == "G"

    def empty_box(self, pos_y, pos_x):
        """ Return position of empty box """
        return self.map[pos_y][pos_x] == " "

    def items_in_box(self, pos_y, pos_x):
        """ Return position of items """
        return self.map[pos_y][pos_x] in ["1", "2", "3"]

    def valid_move(self, pos_y, pos_x):
        """ Testing if move is valid """

        if self.items_in_box(pos_y, pos_x):
            return True

        if self.empty_box(pos_y, pos_x):
            return True

    def counter_items(self, pos_y, pos_x, window):
        """ Counter for items """
        if self.map[pos_y][pos_x] in ["1", "2", "3"]:
            self.total_items += 1

        font_text = pygame.font.SysFont("cosmicsansms", 32)
        text = font_text.render("Items: " + str(self.total_items), True, (255, 255, 255))

        window.blit(text, (360, 4))

    def mg_vs_guardian(self, pos_y, pos_x, window):
        """ check if Mg to all objects to lull the gardian """
        if self.map[pos_y][pos_x] == "G" and self.total_items != 3:
            text_dead = pygame.font.SysFont("cosmicsansms", 32)
            msg_dead = text_dead.render("You are dead! You must recover",
                                        True, (255, 255, 255))
            msg_dead2 = text_dead.render("all the items to lull the guardian",
                                         True, (255, 255, 255))
            window.blit(msg_dead, (22, 150))
            window.blit(msg_dead2, (16, 170))

            self.start_game = 0

        elif self.map[pos_y][pos_x] == "G" and self.total_items == 3:
            text_final = pygame.font.SysFont("cosmicsansms", 32)
            msg_final = text_final.render("Great!! You are free!", True, (255, 255, 255))
            window.blit(msg_final, (50, 190))

            self.start_game = 0

    def user_move(self, window):
        """ User choice one direction for move MacGyver
        Liste of moves : Z,Q,S,D for Up, Left, Down and Right """

        y_values = self.pos_y
        x_values = self.pos_x
        macgyver = pygame.image.load("ressources/MacGyver.png").convert()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_values = self.pos_y + 1
                elif event.key == pygame.K_UP:
                    y_values = self.pos_y - 1
                elif event.key == pygame.K_LEFT:
                    x_values = self.pos_x - 1
                elif event.key == pygame.K_RIGHT:
                    x_values = self.pos_x + 1
            elif event.type == pygame.QUIT:
                exit()

        if self.valid_move(y_values, x_values):
            self.map[self.pos_y][self.pos_x] = " "

            self.pos_y = y_values
            self.pos_x = x_values

        self.counter_items(y_values, x_values, window)
        self.mg_vs_guardian(y_values, x_values, window)
        return window.blit(macgyver, ((self.pos_x * 30), (self.pos_y * 30)))
