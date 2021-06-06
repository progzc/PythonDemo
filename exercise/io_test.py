# 读取磁盘文件的内容
file = open('a.txt', 'r', encoding='UTF-8')
print(file.readlines())
file.close()
