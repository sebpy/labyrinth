#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Class labyrinth with all methods """

#import random


class Labyrinth(object):
    """ Create labyrinth with wall.txt """

    def __init__(self):
        self.map = []  # variable map with list

    def load_map(self):
        """ Open wall.txt file with structure of labyrinth """

        with open('wall.txt', 'r') as laby:  # open wall.txt
            for line in laby:
                i = []  # create l list
                for char in line:
                    if char != "\n":  # del last \n
                        i.append(char)
                self.map.append(i)

    def dislay_map(self, char, pos_character):
        """ Show map
        char = MacGyver
        pos_character = Position of MacGyver """

        line_n = 0  # initialise
        for line in self.map:
            if line_n == pos_character[1]:
                print(line[0:pos_character[0]] + char + line[pos_character[0]+1:])  # Slicing
            else:
                print(line)
            line_n += 1  # incremente line_n

    def items(self):
        """ Randomize 3 items on map """
        pass

    def valid_move(self, pos_x, pos_y):
        """ Testing if move is valid """

        n_line = len(self.map[0])  # count numbers rows
        n_rows = len(self.map)  # count numbers lines

        if pos_x < 0 or pos_y < 0 or pos_x > (n_rows -1) or pos_y > (n_line -1):
            return None
        elif self.map[pos_x][pos_y] == "S":
            return [-1, -1]
        elif self.map[pos_x][pos_y] != " ":
            return None
        else:
            return [pos_y, pos_x]

    def user_move(self, pos_char):
        """ User choice one direction for move MacGyver
        Liste of moves : Z,Q,S,D for Up, Left, Down and Right """

        choice = input("Utiliser les lettres Z (Haut), S (Bas), Q (Gauche), \
        D (Droite)\n Quelle direction? ")
        if choice.upper() == "S":
            pos_char = self.valid_move(POS_CHARACTER[1]+1, POS_CHARACTER[0])
        elif choice.upper() == "Z":
            pos_char = self.valid_move(POS_CHARACTER[1]-1, POS_CHARACTER[0])
        elif choice.upper() == "Q":
            pos_char = self.valid_move(POS_CHARACTER[1], POS_CHARACTER[0]-1)
        elif choice.upper() == "D":
            pos_char = self.valid_move(POS_CHARACTER[1], POS_CHARACTER[0]+1)
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
            POS_CHARACTER[0] = pos_char[0]
            POS_CHARACTER[1] = pos_char[1]


if __name__ == "__main__":

    CHAR = ["M"]
    POS_CHARACTER = [0, 1]

    LAB = Labyrinth()
    LAB.load_map()

    while True:
        LAB.dislay_map(CHAR, POS_CHARACTER)
        LAB.user_move(POS_CHARACTER)
