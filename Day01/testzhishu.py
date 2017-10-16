# coding:utf-8

# 获取0-100之间所有的质数
list1 = []
for i in range(2, 101):
    for j in range(2, i):
        # 假如能被整除，则表示赋值s=1，然后跳出循环
        if i % j == 0:
            break
    else:
        # 如果正常执行完程序，则执行的内容
        # 如果上面的循环只要从break中退出来，
        # 则不会执行else的内容
        list1.append(i)
print list1
