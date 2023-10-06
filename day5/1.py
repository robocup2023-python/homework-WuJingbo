'''
题⽬：编写⼀个函数cacluate，可以接收任意多个数，返回的是⼀个元组。元组的第⼀个值为所有参数的平均值，第⼆个值是⼤于平均值的索引
程序分析：函数的特殊参数：*arg、**kwarg
'''


def calculate(*args):
    average = sum(args) / len(args)
    indexes = [i for i, x in enumerate(args) if x > average]
    return (average, indexes)


result = calculate(1, 2, 3, 4, 5, 6)
print(result)
