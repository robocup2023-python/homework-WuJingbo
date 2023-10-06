'''
题⽬：编写⼀个函数，该函数将获取传⼊的列表的所有奇数位索引对应的元素，并将返回包含所有奇数位元素的列表
'''


def get_odd_index_elements(lst):
    odd_elements = []
    for i in range(len(lst)):
        if i % 2 != 0:
            odd_elements.append(lst[i])
    return odd_elements


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = get_odd_index_elements(my_list)
print(result)
