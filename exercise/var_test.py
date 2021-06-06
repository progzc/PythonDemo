# 变量

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
