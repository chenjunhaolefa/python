
# f(n)=f(n-1)+f(n-2)
list1 = [0, 1]
for i in range(2, 101):
    num = list1[i-1] + list1[i-2]
    list1.append(num)
print list1
