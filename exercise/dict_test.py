# 字典是python内置的数据结构之一，与列表一样是一个可变序列
# 以键值对的方式存储数据，字典是一个无序的序列

# 字典的创建方式
# 使用{}创建字典
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores, type(scores))
# 使用dict()创建字典
student = dict(name='jack', age=20)
print(student, type(student))
# 创建一个空字典
null_dict = {}
print(null_dict)

# 字典中元素的获取
scores = {'张三': 100, '李四': 98, '王五': 45}
# 方式一：使用[]
print(scores['张三'])
# print(scores['陈六'])
# 方式二：使用get()方法
print(scores.get('张三'))
print(scores.get('陈六'))
print(scores.get('陈六', 99))

# 字典中键的判断：in、not in
scores = {'张三': 100, '李四': 98, '王五': 45}
print('张三' in scores)
print('张三' not in scores)

# 字典元素的删除
del scores['张三']
print(scores)
# 清空字典的元素
scores.clear()
print(scores)

# 字典元素的添加
scores = {'张三': 100, '李四': 98, '王五': 45}
print(scores)
scores['陈六'] = 98
print(scores)

# 字典的视图操作
scores = {'张三': 100, '李四': 98, '王五': 97, '王五': 9}
# 获取所有的键
keys = scores.keys()
print(keys, type(keys))
# 将所有的键组成的视图转换成列表
print(list(keys))
# 获取所有的值
values = scores.values()
print(values, type(values))
# 将所有的值转换成列表
print(list(values))
# 获取所有的键值对
items = scores.items()
print(items, type(items))
# 将所有的键值对转换成列表
print(list(items))

# 字典元素的遍历
scores = {'张三': 100, '李四': 98, '王五': 45}
for item in scores:
    print(item, scores[item], scores.get(item))

# 字典的特点：
# 1.字典中的所有元素都是一个key-value对,key不允许重复,value可以重复
d = {'name': '张三', 'name': '李四'}
print(d)
d = {'name': '张三', 'nickname': '张三'}
print(d)
# 2.字典中的元素是无序的
# 3.列表中的key必须是不可变对象
lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)
# d = {lst: 100}
# print(d)
# 4.字典可以根据需要动态地伸缩
# 5.字典会浪费较大的内存，是一种使用空间换时间的数据结构

# 字典生成式
items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85, 100, 120]
lst = zip(items, prices)
print(list(lst))
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
