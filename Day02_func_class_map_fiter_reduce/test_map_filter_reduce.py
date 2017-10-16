# coding=utf-8
# map
# 传入一个函数和多个序列，对于序列的每一个元素，放入函数做处理
# def f(x):
#     return x ** 2
f=lambda x:x**2

list1 = range(1, 20)
# list2 = map(f, list1)
list2 = map(lambda x:x**2,list1)
print list2


# filter
# 传入一个函数和一个序列，对于序列中的每一个元素，传入函数中，把函数返回为true的做保留，其他的全部丢弃

def f1(x):
    return x%2 # 能被整除法，return 0 相当于false

list3 = range(1,20)
list4 = filter(f1,list3)
print list4

# reduce
# 传入一个函数和一个序列，对于序列进行函数的挨个计算并且把之前的结果汇总计算

def f2(x,y):
    return 2*x+y

list5=range(1,5)
num=reduce(f2,list5)
print list5
print num

#help(reduce)
#help(map)
#help(filter)
