#!/usr/bin/env python3

global a

a = 9

def change():
	print(a)

print("Before the functin call", a)

print("Inside the function call", end = ' ')
change()

print("After the function call", a)

