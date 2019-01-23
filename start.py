#! /usr/bin/env python3
# -*- coding: utf8 -*-

#import laby
#import mg_character
#import items

def loadLabyrinth():
	""" Read wall.txt and show labyrinth"""

	wall = open('wall.txt', 'r') # Open file
	readLines = wall.readlines() # Read file line by line
	wallList = [list(i.strip()) for i in readLines] # add line to list

	for i in wallList:
		wallPrint = ''
		for w in i:
			wallPrint = wallPrint + w
		print(wallPrint)



if __name__ == "__main__":
	loadLabyrinth()
	#move()
