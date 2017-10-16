class Animal(object):
    def __init__(self,h,w):
        self.height=h
        self.weight=w
    def say(self):
        pass

class Dog(Animal):
    def say(self):
        print 'wang wang'

dog=Dog(20,10)
dog.say

print Animal.__bases__