file = open('a.txt', 'r', encoding='UTF-8')
# 读取两个字符
# print(file.read(2))

# 读取全部内容
# print(file.read())

# 读取一行，返回字符串
# print(file.readline())

# 读取所有行，返回列表
# print(file.readlines())

# seek读
file.seek(3)
print(file.read())

file.close()
