'''
题⽬：有 n 个整数，使其前⾯各数顺序向后移 m 个位置，最后 m 个数变成最前⾯的 m 个数程序
分析：使⽤列表的pop和insert⽅法实现弹出最后⼀个元素、插⼊⼀个元素到开头
'''

n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(m):
    a.insert(0, a[n-1])
    a.pop()
print(a)
