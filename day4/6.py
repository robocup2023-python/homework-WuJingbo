'''
报错原因：
在循环过程中，使用了列表的pop()方法删除元素。当删除一个元素后，列表的长度发生了变化，但是循环中的索引idx并没有相应地更新。因此，在后续的循环中，会出现索引越界的情况，导致报错。
'''
list = list(range(1000))
for idx in range(len(list)-1, -1, -1):
    if list[idx] % 2 == 1:
        list.pop(idx)
print(list)
