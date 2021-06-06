# object类

class Student:
    # __init__:对创建的对象进行初始化
    def __init__(self, name, age):
        print('__init__被调用了,self的id值为:{0}'.format(id(self)))
        self.name = name
        self.age = age

    # __new__:用于创建对象
    def __new__(cls, *args, **kwargs):
        print('__new__被调用只需了,cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为{0}'.format(id(obj)))
        return obj

    # __str__方法类似于java中的toString方法
    def __str__(self):
        return '我的名字是{0},今年{1}岁了'.format(self.name, self.age)

    # __add__:使对象具有"+"功能
    def __add__(self, other):
        return self.name + other.name

    # __len__:让内置函数的参数可以是自定义类型
    def __len__(self):
        return len(self.name)


stu = Student('张三', 20)
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
'''
print(dir(stu))
print(stu)


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = C('Jack', 20)
# __dict__:获得类对象或实例对象所绑定的所有属性和方法的字典
print(x.__dict__)
print(C.__dict__)
# __class__:输出对象所属的类型
print(x.__class__)
# __bases__:输出父类的元组
print(C.__bases__)
# __base__:输出离的最近父类
print(C.__base__)
# 查看类的层次结构，返回元组类型
print(C.__mro__)
# 查看子类的列表
print(A.__subclasses__())

# __add__:通过重写该方法,可使自定义对象具有"+"的功能
a = 20
b = 100
print(a.__add__(b))
stu1 = Student('张三', 10)
stu2 = Student('李四', 20)
print(stu1 + stu2)
print(stu1.__add__(stu2))

# __len__:重写该方法,让内置函数的参数可以是自定义类型
lst = [11, 22, 33, 44]
print(len(lst))
print(len(stu1))

# __new__:用于创建对象
print('object这个类对象的id为:{0}'.format(id(object)))
print('Student这个类对象的id为:{0}'.format(id(Student)))
stu = Student('张三', 20)
print('stu这个实例对象的id为:{0}'.format(id(stu)))
