#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Start Labyrinth game """


import laby
#import move as mv


if __name__ == "__main__":

    CHAR = ["M"]
    laby.POS_CHARACTER = [0, 1]

    LAB = laby.Labyrinth()
    #MOVING = mv.move()
    LAB.load_map()

    while True:
        LAB.dislay_map()
        #MOVING.user_move(laby.POS_CHARACTER)
        LAB.user_move(laby.POS_CHARACTER)
