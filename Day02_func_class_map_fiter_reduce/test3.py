# coding=utf-8
def h(v):
    return v * 2


def f(g, v):
    print g.__name__  # 输出模块名
    r = g(v)  # 函数调用，g传进来的是一个函数名
    print r


# 调用f
f(h, 3)
