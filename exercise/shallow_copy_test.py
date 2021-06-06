import copy


# 浅拷贝
class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu = CPU()
disk = Disk()
computer = Computer(cpu, disk)
# 浅拷贝：只拷贝源对象，不拷贝子对象
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)
