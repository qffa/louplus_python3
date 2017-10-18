#!/usr/bin/env python3

class Animal(object):

	def __init__(self, name):
		self._name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value

	def make_sound(self):
		pass
	
	@staticmethod
	def order_animal_food():
		print('ording....')
		print('ok')


class Cat(Animal):
	def make_sound(self):
		print(self_name + ' is making sound miu miu miu...')


cat = Cat('kitty')

print(cat.name)


cat.name = 'betty'

print(cat.name)



Animal.order_animal_food()





