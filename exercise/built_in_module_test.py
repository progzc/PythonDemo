# python中的常用的内置模块
import sys
import time
# 文件输入输出
# import os
# import calendar
# 网络请求相关
import urllib.request

# import json
# 正则表达式
# import re
# import math
# import decimal
# import logging

print('----------------使用sys模块---------------------')
# 获取整数24在python中占用的字节大小
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print('----------------使用sys模块---------------------')
# 输出单位为秒
print(time.time())
print(time.localtime(time.time()))

print('----------------使用os模块---------------------')
print(urllib.request.urlopen('http://www.baidu.com').read())
