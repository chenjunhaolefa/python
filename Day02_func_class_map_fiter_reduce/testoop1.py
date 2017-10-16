# coding:utf-8
# 旧式类(经典类)


class A:
    pass

# 实例化
a=A()
print type(a)


# 新式类
class B():
    # 构造函数，实现类初始化
    def __init__(self,name):
        # 初始化 类属性（变量）
        self.Name=name
        print self

b=B('chenjun')
print type(B)
print type(b)
print a.__class__   # 用于显示它的类型

# instance实例化对象
# classobj 类
print A.__doc__
