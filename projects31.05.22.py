### learning python OOP 
import random as rn 
import numpy as np
import sys, os
print(os.listdir())
os.chdir('C:\\*****\\dir')
print(os.listdir())

class Color:
    red=0
    green=0
    blue=0
    
    def __init__(self,r,g,b): #конструктор
        Color.red=r
        Color.green=g
        self.blue=b

    def toHex(self): #метод
        return '%02x%02x%02x'%(Color.red,Color.green,Color.blue)
class ColorBlured(object):
    red=0
    green=0
    blue=0
    alpha=1
    def __init__(self,r,g,b,a):
        self.red=r
        self.green=g
        self.blue=b
        self.alpha=a
   # def __new__(color):
    #    return ColorBlured(color.red,color.green,color.blue,1)
class Square(object):
    
    @staticmethod
    def surpris():
        return 'пошел нахуй'
    #@classmethod другие классы например ??
    @classmethod
    def method(self,x):
        return x*x
    
#a=1
#print(id(a))
#a=2
#print(id(a)) ответы разные да



