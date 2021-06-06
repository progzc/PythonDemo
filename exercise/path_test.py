import os.path

# 获取文件的绝对路径
print(os.path.abspath('path_test.py'))

# 判断文件是否存在
print(os.path.exists('path_test.py'), os.path.exists('path2_test.py'))

# 将目录与目录或者文件名拼接起来
print(os.path.join('E:\\PythonProject', 'PythonDemo'))

# 分离文件名与路径
print(os.path.split('E:\\PythonProject\\PythonDemo\\exercise\\path_test.py'))

# 分离文件名与扩展名
print(os.path.splitext('E:\\PythonProject\\PythonDemo\\exercise\\path_test.py'))

# 从一个目录中提取文件名
print(os.path.basename('E:\\PythonProject\\PythonDemo\\exercise\\path_test.py'))

# 从一个路径中提取文件路径，不包括文件名
print(os.path.dirname('E:\\PythonProject\\PythonDemo\\exercise\\path_test.py'))

# 判断是否是路径
print(os.path.isdir('E:\\PythonProject\\PythonDemo\\exercise\\path_test.py'))
