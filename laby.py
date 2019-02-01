#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Class labyrinth with all methods """

import random as rd


class Labyrinth(object):
    """ Create labyrinth with wall.txt """

    def __init__(self):
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
        while len(i) > 0:
            pos_y = rd.randint(0, 8)  # generates a number between 0 and the number of rows
            pos_x = rd.randint(0, 14)  # generates a number between 0 and the number of col
            if self.map[pos_y][pos_x] == " ":
                self.map[pos_y][pos_x] = i[0]
                i.pop(0)

    def dislay_map(self):
        """ Show map """

        line_n = 0  # initialise
        for line in self.map:
            print("".join(line))  # show laby without [""]
            line_n += 1  # increment line_n

    def valid_move(self, pos_y, pos_x):
        """ Testing if move is valid """

        if pos_x < 0 or pos_y < 0 or pos_y > 9 or pos_x > 14:
            return None
        elif self.map[pos_x][pos_y] == "G":
            if self.total_items != 3:
                self.map[pos_x][pos_y] = " "
                print("Vous devez récupérer tout les objets pour endormir le gardien")
                exit()
            else:
                return [-1, -1]
        elif self.map[pos_y][pos_x] == "1" or self.map[pos_y][pos_x] == "2" or self.map[pos_y][pos_x] == "2":
            self.total_items += 1  # Increment count
            self.map[pos_y][pos_x] = " "  # replace empty space if item is picked
            return [pos_y, pos_x]  # return position of MG

        elif self.map[pos_y][pos_x] != " ":
            return None  # return None if move impossible
        else:
            return [pos_y, pos_x]  # return position of MG

    def user_move(self):
        """ User choice one direction for move MacGyver
        Liste of moves : Z,Q,S,D for Up, Left, Down and Right """

        print("Objet ramassés: " + str(self.total_items))
        choice = input("Utiliser les lettres Z (Haut), S (Bas), Q (Gauche), \
        D (Droite)\n Quelle direction? ")
        if choice.upper() == "S":
            pos_char = self.valid_move(self.pos_y + 1, self.pos_x)
        elif choice.upper() == "Z":
            pos_char = self.valid_move(self.pos_y - 1, self.pos_x)
        elif choice.upper() == "Q":
            pos_char = self.valid_move(self.pos_y, self.pos_x - 1)
        elif choice.upper() == "D":
            pos_char = self.valid_move(self.pos_y, self.pos_x + 1)
        elif choice.upper() == "X":
            exit()
        else:
            print("Seul les touche de déplacement Z,Q,S,D et X pour quitter sont authorisés")

        if pos_char is None:
            print("Déplacement impossible")
        elif pos_char == [-1, -1]:
            print("Super! Vous vous êtes échappé!")
            return exit()
        else:
            
            self.pos_y = pos_char[0]
            self.pos_x = pos_char[1]


if __name__ == "__main__":

    LAB = Labyrinth()
    LAB.load_map()
    LAB.randomize_items()

    while True:
        LAB.dislay_map()
        LAB.user_move()
