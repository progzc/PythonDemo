# 模块
# 导入模块的几种方式
# 方式一：import 模块名称 [as 别名]
# 方式二：from 模块名称 import 函数/变量/类
import math
from math import pi, pow

# 导入自定义模块
import calc
from calc import div

print(id(math))
print(type(math))
print(math)
print(math.pi)

# 查看math模块提供的属性、类和函数
print(dir(math))
print(math.pow(2, 3), type(math.pow(2, 3)))
print(math.ceil(9.001))
print(math.floor(9.9999))

print(pi)
print(pow(2, 3))

# 使用自定义模块
print(calc.add(1, 2))
print(div(1, 2))
