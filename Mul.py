n = 10
for n in range(1, n):
    for i in range(1, n+1):
        #print str(i) + '*' + str(n) + '=' + str(i*n),
        print '%d * %d = %-2d' % (i, n, i * n),
    print
