# os模块与操作系统相关
import os

# 打开记事本
# os.system('notepad.exe')

# 打开计算器
# os.system("calc.exe")

# 直接调用可执行文件
# os.startfile('D:\\ProgramFiles\\WeChat\\WeChat.exe')

# 返回当前的工作目录
print(os.getcwd())

# 返回指定路径下的而文件和目录信息，返回列表
print(os.listdir('./package'))

# 创建目录
# os.mkdir('newdir')
# 创建多级目录
# os.makedirs('newdir2/dir2')

# 删除目录
# os.rmdir('newdir')
# 删除多级目录
# os.removedirs('newdir2/dir2')

# 将path设置为当前的工作目录
os.chdir('E:\\PythonProject\\PythonDemo')
print(os.getcwd())
