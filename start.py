#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Start Labyrinth game """


import laby
#import move as mv


if __name__ == "__main__":

    CHAR = ["M"]
    laby.pos_character = [0, 1]

    LAB = laby.Labyrinth()
    #MOVING = mv.move()
    LAB.load_map()

    while True:
        LAB.dislay_map(CHAR, laby.pos_character)
        #MOVING.user_move(laby.pos_character)
        LAB.user_move(laby.pos_character)
