#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Start Labyrinth game """

import laby
import display


def main():
    """ Main function"""

    disp = display.Display()
    lab = laby.Labyrinth()
    lab.load_map()
    lab.randomize_items()
    disp.display_map(lab.map)
    disp.display_flip()

    while True:
        disp.counter(lab.total_items)
        disp.clean_box(lab.pos_y, lab.pos_x)
        lab.user_move()
        disp.mac_gyver(lab.pos_y, lab.pos_x)
        disp.display_flip()

        if lab.dead == 1:
            disp.message(disp.msg_dead)
            disp.display_flip()
            break
        elif lab.free == 1:
            disp.message(disp.msg_free)
            disp.display_flip()
            break


if __name__ == "__main__":
    main()
