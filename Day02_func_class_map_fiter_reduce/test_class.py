# coding=utf-8
import json


class People:
    'This is a test'
    head = 1

    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def getName(self):
        print self.Name


people = People(u'张三', 20)
people2 = People(u'李四',21)
people.getName()
people.head = 2
print 'People:',People.head
print 'people:',people.head
print 'people2:',people.head
print people.__dict__
# print json.dump(people.__dict__, ensure_ascii=False, encoding='gbk')
print people.__doc__
print people.__class__

# 类的魔术方法
class C:
    def __getattr__(self, name):
        self.__dict__[name]='a'
        return name
    def __setattr__(self,name,value):
        self.__dict__[name]=value

c=C()
print c.a
c.b='1'
print c.__dict__
