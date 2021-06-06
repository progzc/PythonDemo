# 封装
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()
print(stu.name)
# 在类的外部不能直接访问私有属性
# print(stu.__age)

# 打印stu对象所包含的所有内容
print(dir(stu))
# 在类的外部通过其他方法访问私有属性（不推荐）
print(stu._Student__age)
