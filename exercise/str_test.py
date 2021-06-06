import sys

# PyCharm对字符串进行了优化处理：导致交互模式和IDE模式的不同

print('-----------------字符串的驻留机制----------------------')
# 字符串的驻留机制
a = 'Python'
b = "Python"
c = '''Python'''
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 交互模式与IDE模式的区别
s1 = 'abc%'
s2 = 'abc%'
print(s1 is s2)

# 比较编译时和运行时的区别
a = 'abc'
b = 'ab' + 'c'
print(a is b)
c = ''.join(['ab', 'c'])
print(a is c)

# -5~256数字是驻留的：交互模式与IDE模式的区别
a = 256
b = 256
print(a is b)
a = -6
b = -6
print(a is b)

# 强制驻留：交互模式与IDE模式的区别
c = ''.join(['ab', 'c'])
a = sys.intern(c)
print(a is c)

print('-----------------字符串的查询操作----------------------')
# 查找子串第一次出现的位置，找不到会抛出异常
s = 'hello,hello'
print(s.index('lo'))
# 查找子串第一次出现的位置，找不到会返回-1
print(s.find('lo'))
# 查找子串最后一次出现的位置，找不到会抛出异常
print(s.rindex('lo'))
# 查找子串最后一次出现的位置，找不到会返回-1
print(s.rfind('lo'))

print('-----------------字符串的大小写转换操作----------------------')
s = 'hello,python'
# 转大写
a = s.upper()
print(a, id(a))
print(s, id(s))
# 转小写
b = s.lower()
print(b, id(b))
print(b == s)
print(b is s)
# 大转小，小转大
s2 = 'hello,Python'
print(s2.swapcase())
# 首字符大写，其他小写
print(s2.capitalize())
# 每个单词首字母大写
print(s2.title())

print('-----------------字符串内容对齐的操作----------------------')
s = 'hello,Python'
# 居中对齐
print(s.center(20, '*'))
# 左对齐
print(s.ljust(20, '*'))
print(s.ljust(10))
print(s.ljust(20))
# 右对齐
print(s.rjust(20, '*'))
print(s.rjust(10))
print(s.rjust(20))
# 右对齐，会使用0进行填充
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))

print('-----------------字符串劈分操作----------------------')
s = 'hello world Python'
s1 = 'hello|world|Python'
# 从左边开始劈分，返回列表
print(s.split())
print(s1.split(sep='|'))
print(s1.split(sep='|', maxsplit=1))
# 从右边开始劈分，返回列表
print(s1.rsplit(sep='|', maxsplit=1))

print('-----------------判断字符串的操作----------------------')
s = 'hello,python'
# 判断是否是合法的标识符
print(s.isidentifier())
print('hello'.isidentifier())
print('张三_'.isidentifier())
print('张三_123'.isidentifier())
# 判断是否由空白字符组成（回车、换行、水平制表符）
print('\t'.isspace())
# 判断是否全部由字母组成
print('abc'.isalpha())
# 判断是否全部由十进制组成
print('123'.isdecimal())
print('123四'.isdecimal())
# 判断是否全部由数字组成
print('123'.isnumeric())
print('123四'.isnumeric())
# 判断是否全部由字母或数字组成
print('abc1'.isalnum())
print('abc!'.isalnum())

print('-----------------字符串的其他操作----------------------')
# 替换
s = 'hello,Python'
print(s.replace('Python', 'Java'))
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python', 'Java', 2))
# 将列表或元组中字符串合并成一个字符串
lst = ['hello', 'java', 'Python']
print('|'.join(lst))
print(''.join(lst))
t = ('hello', 'Java', 'Python')
print(''.join(t))
print('*'.join('Python'))

print('-----------------字符串的比较操作----------------------')
print('apple' > 'app')
print('apple' > 'banana')
# 获取字符的原始值
print(ord('a'), ord('b'))
# 根据原始值获取字符
print(chr(ord('a')))
# ==比较值，is比较id
a = b = 'Python'
c = 'Python'
print(a == b, b == c, a is b, b is c, id(a), id(b), id(c))

print('-----------------字符串的切片操作----------------------')
s = 'hello,Python'
s1 = s[:5]
s2 = s[6:]
s3 = s[:]
s4 = s[1:5:2]
s5 = s[::2]
s6 = s[::-1]
s7 = s[-6::1]
print(s, id(s))
print(s1, id(s1))
print(s2, id(s2))
print(s3, id(s3))
print(s4, id(s4))
print(s5, id(s5))
print(s6, id(s6))
print(s7, id(s7))

print('-----------------字符串的格式化操作----------------------')
# 方式一：%占位符
name = '张三'
age = 20
print('我叫%s,今年%d岁' % (name, age))
# 指定宽度
print('%10d' % 99)
# 指定精度
print('%.3f' % 3.1415926)
# 同时表示宽度和精度
print('%10.3f' % 3.1415926)
# 方式二：{}占位符
print('我叫{0},今年{1}岁'.format(name, age))
print('{0:10.3f}'.format(3.1415926))
print('{:10.3f}'.format(3.1415926))
# 方式三：f-string
print(f'我叫{name},今年{age}岁')

print('-----------------字符串的编码转换----------------------')
# 编码
s = '天涯共此时'
print(s.encode(encoding='GBK'))
print(s.encode(encoding='UTF-8'))
# 解码
byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
