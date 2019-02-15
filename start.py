#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Start Labyrinth game """

import pygame
import laby
import display


def main():
    """ Main function"""

    disp = display.Display()
    lab = laby.Labyrinth()
    lab.load_map()
    lab.randomize_items()

    disp.window.blit(disp.msg_load, (40, 220))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lab.start_game = 1
                elif event.key == pygame.K_q:
                    exit()

        while lab.start_game:
            disp.display_map(lab.map)
            disp.counter(lab.total_items)
            disp.mac_gyver(lab.pos_y, lab.pos_x)
            lab.user_move()
            pygame.display.flip()

        if lab.dead == 1:
            disp.message(disp.msg_dead)
            pygame.display.flip()
            break


if __name__ == "__main__":
    main()
