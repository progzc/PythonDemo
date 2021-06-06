# 继承
# python支持多重继承

# 默认继承object类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name, self.age))


# 定义子类
class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no
        print(self.stu_no)

    def info(self):
        super().info()
        print('学号:{0}'.format(self.stu_no))


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

    def info(self):
        super().info()
        print('教龄:{0}'.format(self.teachofyear))


# 多重继承
class A(object):
    pass


class B(object):
    pass


class C(A, B):
    pass


# 测试
stu = Student('jack', 20, '1001')
stu.info()
teacher = Teacher('李四', 34, 10)
teacher.info()
