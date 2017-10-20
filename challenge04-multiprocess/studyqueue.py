#!/usr/bin/env python3

from multiprocessing import Process, Queue


queue = Queue()


def f1():
	queue.put('hello shiyanlou')
	queue.put("hello qff")


def f2():
	data = queue.get()
	print(data)
	data = queue.get()
	print(data)




Process(target=f1).start()
Process(target=f2).start()
