# coding:utf-8
for i in range(21):
    for j in range(34):
        for k in range(0, 101, 3):
            if i + j + k == 100 and 5 * i + 4 * j + k / 3 == 100:
                print '买了%d只公鸡，%d只母鸡，%d只小鸡'%(i, j, k)

print str(range(0, 20, 3))