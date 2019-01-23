# -*- coding: utf8 -*-

# import random

class Labyrinth():
	""" Cette class regroupe toutes les méthodes et attributs de l'objet labyrinth """

	with open('wall.txt', r) as w:
		data = w.readlines()
		w.close()

	for i in range(len(data)):
		data[i] = data[i].strip()
		return tuple(data)
