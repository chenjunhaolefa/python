# coding=utf-8
import numpy as np
#help(np.array)

print np.zeros((6,6))

print np.empty((4,4))

print np.arange(1,10)
print np.array(range(1,10))

print '生成一个等差数列,endpoint参数可以设置是否包含最后一个节点:',\
    np.linspace(1,10,5,endpoint=False)
print np.linspace(1,10,6)

print '生成一个等比数列,默认是生成以10为底的log值:',\
    np.logspace(1,10,6).astype(int)


print np.random.random((2,3,4))

print '生成随机范围内的随机整数:',\
    np.random.randint(1,10,(2,3,4))
print '生成指定形状的随机数位于【0-1】:',np.random.rand(3,2)
print '生成指定形状的标准正态分布随机数',np.random.randn(3,2)

print '生成一个种子:'
np.random.seed(4)
print np.random.rand(4)
print np.random.randn(4)

print '生成高斯分布的随机数,loc代表次概率分布的均值,scale次概率分布的标准差,size形状,\
       从某个分布，由均值和标准差标识中获得样本:',\
    np.random.normal(0,1,100)

a2=np.array([1,2,3,4])
print a2.dtype
print a2.astype(float)

print '数据类型-字符串:',\
    np.array(['aabbccddee','abcde'],dtype='|S5')


a1 = np.array([5,6,7,8])
print 'test:',a1+a2

arr=np.arange(40).reshape(5,-1)
print arr
# 转置
np1=np.arange(8).reshape(2,2,-1)
print np1.transpose()
print '*'*30
print np1



