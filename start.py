#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Start Labyrinth game """

import pygame

import laby

sprite_size = 30
sprite_n = 15
board_size = sprite_size * sprite_n

pygame.init()
pygame.display.set_caption("Help Mac Gyver to escape!")

window = pygame.display.set_mode((board_size, board_size))
text_load = pygame.font.SysFont("cosmicsansms", 32)
msg_load = text_load.render("To play, press ENTER", True, (255, 255, 255))

if __name__ == "__main__":
    launch_game = 1
    while launch_game:
        lab = laby.Labyrinth()
        lab.load_map()
        lab.randomize_items()
        pygame.key.set_repeat(400, 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launch_game = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lab.start_game = 1

        window.blit(msg_load, (50, 220))
        pygame.display.flip()

        while lab.start_game:
            lab.display_map(window)
            lab.user_move(window)
            pygame.display.flip()
