#!/usr/bin/env python3

class A(object):
    def __init__(self,name):
        self.name = name

    def getname():
        return "<name=%s>" %self.name

a = A('qff')

print(a.getname())
