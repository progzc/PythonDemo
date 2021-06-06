# 列表特点如下：
# 列表有序
# 索引正向从0开始，逆向从-1开始
# 可以存储重复数据
# 任意数据类型混存
# 根据需要动态分配和回收内存

# 第一种方式
lst = ['hello', 'world', 98]
print(id(lst))
print(type(lst))
print(lst)

# 第二种方式
lst2 = list(['hello', 'world', 98, 'hello'])
print(lst2)
print(lst2[0])
print(lst2[-1])
# 元素有多个则只返回第一个的索引
print(lst2.index('hello'))
# 若不存在会抛出异常
# print(lst.index('Python'))
# 在指定范围查找
print(lst2.index('hello', 1, 4))

# 列表切片
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print('原列表', id(lst))
print('切片', id(lst[1:6:2]))
print(lst[1:6:2])
print(lst[1:6:])
print(lst[:6:2])
print(lst[:6:])
print(lst[1::2])
# 步长为负数
print(lst[::-1])
print(lst[7::-1])
print(lst[6:0:-2])

# 判断元素在列表中是否存在
lst = [10, 20, 'python', 'hello']
print(10 in lst)
print(10 not in lst)

# 列表元素的遍历
for item in lst:
    print(item)

# 在列表的末尾添加一个元素
lst = [10, 20, 30]
print('添加元素之前', lst, id(lst))
lst.append(100)
print('添加元素之后', lst, id(lst))
# 在列表的末尾至少添加一个元素
lst2 = ['hello', 'world']
# lst.append(lst2)
lst.extend(lst2)
print(lst)
# 在指定位置插入元素
lst.insert(1, 90)
print(lst)
# 在任意位置上切片替换
lst3 = [True, False, 'hello']
lst[1:] = lst3
print(lst)

# 列表的删除操作
lst = [10, 20, 30, 40, 50, 60, 30, 60]
# 重复元素只删除第一个
lst.remove(30)
print(lst)
# 根据索引移除元素
lst.pop(1)
print(lst)
# 移除列表最后的一个元素
lst.pop()
print(lst)
lst.pop(-1)
print(lst)
# 切片：删除至少一个元素，将产生一个新的列表对象
new_lst = lst[1:3]
print('原列表', lst)
print('切片后的列表', new_lst)
# 不产生新的切片
lst[1:3] = []
print(lst)
# 清除列表中的所有元素
lst.clear()
print(lst)
# 删除列表
del lst
# print(lst)

# 修改列表元素
lst = [10, 20, 30, 40]
# 一次修改一个值
lst[2] = 100
print(lst)
# 一次修改多个值
lst[1:3] = [300, 400, 500, 600]
print(lst)

# 列表元素的排序
lst = [20, 40, 10, 98, 54]
print('排序前的列表', lst, id(lst))
lst.sort()
print('排序后的列表', lst, id(lst))
# 降序排序
lst.sort(reverse=True)
print('降序后的列表', lst, id(lst))
# 使用内置函数sorted()对列表进行排序，将产生一个新的列表对象
lst = [20, 40, 10, 98, 54]
print('原列表', lst, id(lst))
new_lst = sorted(lst)
print('升序列表', new_lst, id(new_lst))
new_lst2 = sorted(lst, reverse=True)
print('降序列表', new_lst2, id(new_lst2))

# 列表生成式
lst = [i for i in range(1, 10)]
print(lst)
lst = [i * i for i in range(1, 10)]
print(lst)
lst = [i * 2 for i in range(1, 6)]
print(lst)
