#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Start Labyrinth game """

import laby

if __name__ == "__main__":

    LAB = laby.Labyrinth()
    LAB.load_map()
    LAB.randomize_items()
    LAB.start_game()
