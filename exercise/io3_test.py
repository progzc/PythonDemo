file = open('a.txt', 'a', encoding='UTF-8')
# 写字符串
# file.write('\nhello')

# 写列表
# file.writelines(['\njava', '\ngo', '\npython'])

# flush
file.write('\n北京')
file.flush()
file.write('\n上海')
file.close()
