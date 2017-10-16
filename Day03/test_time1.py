# coding=utf-8
import time

# 返回当前时间的时间戳
# 从1970年1月1日零点零分零秒至今的秒数
print time.time()
# 接收我们当前的时间戳返回对应的时间元组
print time.localtime(time.time())
print time.localtime()
print '格林威治时间：',time.gmtime()
print '接收时间元组并返回一个可读形式的字符串:',time.asctime(time.localtime(time.time()))

print '接收时间元组并返回一个可读形式的时间字符串，时间格式由fmt决定:',\
    time.strftime("%Y-%m-%d %H:%M:%S 一年中的第%j天",time.localtime())

print time.strftime('%Z',time.localtime())
print time.strptime('2017032123','%Y%m%d%H%M%S')
print '返回cpu运行时间:',time.clock()