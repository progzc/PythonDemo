for item in 'Python':
    print(item)

for i in range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为_
for _ in range(5):
    print('人生苦短，我用Python')

sum = 0
for item in range(1, 101):
    if sum % 2 == 0:
        sum += item
print('1到100之间的偶数和为:', sum)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, end='\t')
    print()

# for-else
for item in range(3):
    pwd = input('请输入密码:')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起，三次密码均输入错误')

# while-else
# 略
