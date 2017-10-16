# coding=utf-8
import json

str = 'chenjun alice ben'


def f(str2):
    return str2.capitalize()


print ','.join(map(f, str.split()))

name = ['chenjun', 'alice', 'ben']
age = [20, 25, 20]
sex = [u'男', u'女', u'男']
temp = map(lambda x, y, z: (x, y, z), name, age, sex)
print json.dumps(temp, ensure_ascii=False, encoding='gbk')
print temp

list1 = ['a', 'b', 'c']
list2 = range(1, 4)


def f(x, y):
    return (x, y)


list3 = map(f, list1, list2)
print 'list3:', list3
# 类似于如下过程
# zip相当于压缩多个序列，然后形成一个可迭代对象
# for循环一次从这两个序列中，挨个取出同一个索引值对应的不同的数据
list4 = []
for x, y in zip(list1, list2):
    print x, y
    list4.append((x, y))

print 'list4:', list4
# print 'list5:',zip(list1,list2)


x = range(1, 4)
y = ['a', 'b', 'c']
print 'zip(y,x):', zip(y, x)
