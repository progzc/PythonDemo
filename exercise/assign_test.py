# 变量的赋值

class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值操作，只是形成两个变量，实际上还是指向同一个对象
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(id(cpu1))
print(cpu2)
print(id(cpu2))
