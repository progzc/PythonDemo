# present = input('大圣想要什么礼物呢？')
# print(present, type(present))

print(1 + 1)
print(1 - 1)
print(2 * 4)
print(1 / 2)  # 0.5
print(11 / 2)  # 5.5
print(11 // 2)  # 5
print(11 % 2)  # 1

print(9 // 4)  # 2
print(-9 / -4)  # 2
print(9 // -4)  # -3 向下取整
print(-9 // 4)  # -3

print(9 % -4)  # -3 余数 = 被除数 - 除数 * 商
print(-9 % 4)  # 3 余数 = 被除数 - 除数 * 商

a = 3 + 4
b = c = d = 20  # 链式赋值
print(b, id(b))
print(c, id(c))
print(d, id(d))
e, f, g = 20, 30, 40  # 解包赋值
h = 10
print(h, type(h))
h /= 3
print(h, type(h))

m = 1
n = 2
m, n = n, m
print(m, n)

# ==用于比较对象的值,is用于比较对象的标识

a, b = 1, 2
print(a == 1 and b < 2)
print(a == 1 or b < 2)
print(not a == 1)
s = 'helloworld'
print('h' in s)
print('k' not in s)

print(4 | 8)
print(4 & 8)
print(4 ^ 8)

print(1 >> 2)
print(1 << 2)

print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(list()))
print(bool(()))
print(bool(tuple()))
print(bool({}))
print(bool(dict()))
print(bool(set()))

