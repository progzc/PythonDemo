# 集合

print('-----------------集合的创建---------------------------')
# 方式一：直接{}
s = {2, 3, 4, 5, 5, 6, 7, 7}
print(s, type(3))
# 方式二：使用内置函数set()
s2 = set(range(6))
print(s2, type(s2))
# 将列表转化为集合
s3 = set([1, 2, 3, 4, 5, 5, 5, 6, 6])
print(s3, type(s3))
# 将元组转化为集合
s4 = set((1, 2, 4, 4, 5, 65))
print(s4, type(s4))
# 将字符串序列转化为集合
s5 = set('Python')
print(s5, type(s5))
# 创建空集合
s6 = set()
print(s6, type(s6))
# 方式三：集合生成式
s = {i * i for i in range(10)}
print(s, type(s))

print('-----------------集合元素的判断操作---------------------------')
s = {10, 20, 30, 40, 50, 60}
print(10 in s)
print(10 not in s)

print('-----------------集合元素的新增操作---------------------------')
s = {10, 20, 30, 40, 50, 60}
# 添加单个元素
s.add(90)
print(s)
# 至少添加一个元素
s.update({200, 400, 300})
print(s)
s.update([80, 81, 82])
print(s)
s.update((90, 91, 92))
print(s, len(s))

print('-----------------集合的删除操作---------------------------')
# 删除指定元素，不存在就抛出异常
s.remove(200)
print(s, len(s))
# 删除指定元素，不存在不抛出异常
s.discard(500)
print(s, len(s))
# 删除任意一个元素
s.pop()
print(s, len(s))
# 清空集合
s.clear()
print(s)

print('-----------------集合间的关系---------------------------')
# 判断集合是否相等：==或!=
s1 = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s1 == s2)
# 判断子集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))
print(s3.issubset(s1))
# 判断超集
print(s1.issuperset(s2))
print(s1.issuperset(s3))
# 判断是否有交集：有交集是false
print(s2.isdisjoint(s3))

print('-----------------集合的数学操作---------------------------')
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
# 交集
print(s1.intersection(s2))
print(s1 & s2)
# 并集
print(s1.union(s2))
print(s1 | s2)
# 差集
print(s1.difference(s2))
print(s1 - s2)
print(s2.difference(s1))
print(s2 - s1)
# 对称差集
print(s1.symmetric_difference(s2))
print((s1 - (s1 & s2)) | (s2 - (s1 & s2)))
