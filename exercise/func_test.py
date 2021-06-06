# 函数

def calc(a, b):
    c = a + b
    return c


print('----------------------参数的传递的两种方式--------------------------')
# 传参方式一：位置实参
result = calc(10, 20)
print(result)
# 传参方式二：关键字实参
result = calc(b=10, a=15)
print(result)


def fun(arg1, arg2):
    print('arg1', arg1)
    print('arg2', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)


print('----------------------值传递--------------------------')
n1 = 11
n2 = [22, 33, 44]
fun(n1, n2)
print('n1', n1)
print('n2', n2)


def odd_even(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


print('----------------------函数的返回值--------------------------')
lst = [10, 29, 34, 23, 44, 53, 55]
# 函数若有多个返回值，则返回值是元组；若只有一个返回值，则直接返回原值
print(odd_even(lst))
a, b = odd_even(lst)
print(a, b)


def add(a, b=10):
    return a + b


print('----------------------函数参数的默认值--------------------------')
print(add(10))
print(add(10, 20))


# 使用*定义的可变位置参数是一个元组
# 可变位置参数只能有一个
def variable(*args):
    print(args)


# 使用**定义的可变关键字参数是一个字典
# 可变关键字参数只能有一个
def variable2(**args):
    print(args)


print('----------------------可变的位置参值--------------------------')
variable(10)
variable(10, 30)
variable(10, 30, 50)
variable2(a=10)
variable2(a=10, b=30, c=40)


def call_fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


print('----------------------函数的调用--------------------------')
# 将列表中的每个元素都转换为位置实参传入
lst = [11, 22, 33]
call_fun(*lst)
# 将字典中的每个键值对都转换为关键字实参传入
dic = {'a': 111, 'b': 222, 'c': 333}
call_fun(**dic)
