# 变量
name = '玛丽亚'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)


def fun(a, b):
    # 局部变量
    c = a + b
    print(c)


# 全局变量
name = '杨老师'


def fun2():
    # 使用global在函数内部定义全局变量
    global age
    age = 20
    print(name)


fun2()
print(age)
