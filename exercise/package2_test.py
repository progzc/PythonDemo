# 使用import方式进行导入时，只能跟包名或模块名称
# import 包名
import calc2
# import 模块名
import package.module_a
# import 包名+取别名
import package.module_b as mb
# from 包名 import 模块名
# 使用from...import方式可以导入包、模块、函数、变量
from package import module_a

print(package.module_a.a)
print(mb.b)
print(module_a.a)
print(calc2.add(10, 20))
