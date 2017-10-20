#!/usr/bin/env python3

from multiprocessing import Process, Queue

class A(object):

	d1 = {}
	d2 = []
	d3 = ''
	
	def set_data(self,data):
		
		self.d1[0] = data
		self.d2.append(data)
		self.d3 = data

q = Queue()

def f1():

	a = A()
	a.set_data('test data')
	q.put(a)

def f2():

	a = q.get()
	print('a.d1 = ', a.d1)
	print('a.d2 = ', a.d2)
	print('a.d3 = ', a.d3)

def main():

	Process(target=f1).start()
	Process(target=f2).start()

if __name__ == '__main__':

	main()



