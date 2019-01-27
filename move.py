#!/usr/bin/env python3
# -*- coding: utf8 -*-

class move:
    """ Manage movement in game """

    def __init__(self):
        self.pos_character = []

    def valid_move(self, pos_x, pos_y):
        """ Testing if move is valid """

        n_rows = len(self.map[0]) # count numbers rows
        n_line = len(self.map) # count numbers lines

        if pos_x < 0 or pos_y < 0 or pos_x > (n_rows - 1) or pos_y > (n_line - 1): # check postition is in board
            return None
        elif map[pos_x][pos_y] != " ":
            return None
        else:
            return [pos_y, pos_x]

    def user_move(self, pos_char):
        """ User choice one direction for move MacGyver
        Liste of moves : Z,Q,S,D for Up, Left, Down and Right """

        #choice = input("Utiliser les lettres Z (Haut), S (Bas), Q (Gauche), D (Droite)\n Quelle direction? ")
        #if choice.upper() == "Z":
         #   pos_char = self.valid_move(self.pos_character[1]+1,self.pos_character[0])
        #elif choice.upper() == "S":
        #    pos_char = self.valid_move(self.pos_character[1]-1, self.pos_character[0])
        #elif choice.upper() == "Q":
        #    pos_char = self.valid_move(self.pos_character[1], self.pos_character[0]-1)
        #elif choice.upper() == "D":
        pos_char = self.pos_character[1], self.pos_character[0]
        #elif choice.upper() == "X":
         #   exit()

        #if pos_char is None:
            #print("Déplacement impossible")
        print()
        #else:
            #print(pos_char)
            #self.pos_character[0] = pos_char[0]
            #self.pos_character[1] = pos_char[1]

