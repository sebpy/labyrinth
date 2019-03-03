#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Class labyrinth with all methods """

import random as rd
import pygame


class Labyrinth:
    """ Create labyrinth with wall.txt """

    def __init__(self):
        self.dead = 0
        self.free = 0
        self.map = []
        self.total_items = 0
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

        if self.items_in_box(pos_y, pos_x) or self.empty_box(pos_y, pos_x):
            return self.map[pos_y][pos_x]
        return None

    def counter_items(self, pos_y, pos_x):
        """ Counter for items """
        if self.map[pos_y][pos_x] in ["1", "2", "3"]:
            self.total_items += 1

    def mg_vs_guardian(self, pos_y, pos_x):
        """ check if Mg to all objects to lull the gardian """

        if self.map[pos_y][pos_x] == "G" and self.total_items != 3:
            self.dead = 1

        elif self.map[pos_y][pos_x] == "G" and self.total_items == 3:
            self.free = 1

    def user_move(self):
        """ User choice one direction for move MacGyver
        Liste of moves : Z,Q,S,D for Up, Left, Down and Right """

        y_values = self.pos_y
        x_values = self.pos_x

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

        self.counter_items(y_values, x_values)
        self.mg_vs_guardian(y_values, x_values)
        return self.pos_x, self.pos_y
