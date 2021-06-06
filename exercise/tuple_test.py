# 元组：不可变序列

# 元组的创建
# 方式一：使用小括号
t = ('Python', 'world', 98)
print(t, type(t))
# 可以省略小括号
t2 = 'Python', 'world', 98
print(t2, type(t2))
# 只包含一个元素的元组需要使用逗号和小括号，否则是本身的数据类型
t3 = ('Python')
print(t3, type(t3))
t4 = ('Python',)
print(t4, type(t4))
# 方式二：使用内置函数tuple()
t = tuple(('Python', 'world', 98))
print(t, type(t))

# 空元组的创建
t1 = ()
print(t1, type(t1))
t2 = tuple()
print(t2, type(t2))
# 空列表的创建
l1 = []
print(l1, type(l1))
l2 = list()
print(l2, type(l2))
# 空字典的创建
d1 = {}
print(d1, type(d1))
d2 = dict()
print(d2, type(d2))

# 元组的不可变性
t = (10, [20, 30], 9)
print(t, type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))
t[1].append(100)
print(t[1], type(t[1]), id(t[1]))

# 元组的遍历
t = ('Python', 'world', 98)
for item in t:
    print(item)
