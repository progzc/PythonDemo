# 第一种方式
r1 = range(10)
print(r1)  # range(0, 10)
print(list(r1))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 第二种方式
r2 = range(1, 10)
print(list(r2))

# 第三种方式
r3 = range(1, 10, 2)
print(list(r3))
print(10 in r3)
print(10 not in r3)

sum = 0
a = 1
while a <= 100:
    if not bool(a % 2):
        sum += a
    a += 1
print('1-100之间的偶数和', sum)
