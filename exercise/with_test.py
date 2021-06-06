# with语句可以自动管理上下文资源，
# 不论什么原因跳出with块，都能保证文件正确的关闭，以此来达到释放资源的目的

"""
MyContentMgr实现了特殊方法__enter__、__exit__，
则称该类对象遵守了上下文管理器
"""


class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        # print('show方法被调用执行了', 1 / 0)
        print('show方法被调用执行了')


print(type(open('a.txt', 'r', encoding='UTF-8')))
print(dir(open('a.txt', 'r', encoding='UTF-8')))
# 原理是：_io.TextIOWrapper类实现了__enter__和__exit__方法，
# 离开运行时上下文，会自动调用上下文管理器的特殊方法__exit__（即使抛出了异常仍会执行）
with open('a.txt', 'r', encoding='UTF-8') as file:
    print(file.read())

with MyContentMgr() as file:
    file.show()

# 复制文件
with open('a.txt', 'rb') as src_file:
    with open('copy2_a.txt', 'wb') as target_file:
        target_file.write(src_file.read())
