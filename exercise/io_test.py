# 读取磁盘文件的内容
file = open('a.txt', 'r', encoding='UTF-8')
print(file.readlines())
file.close()

# 写入文件到磁盘
file = open('b.txt', 'w')
file.write('Python')
file.close()

# 追加到文件
file = open('b.txt', 'a')
file.write('\ngolang\njava')
file.close()

# 文件的复制
src_file = open('a.txt', 'rb')
target_file = open('copy_a.txt', 'wb')
target_file.write(src_file.read())
src_file.close()
target_file.close()
