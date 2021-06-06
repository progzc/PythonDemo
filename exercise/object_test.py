# object类

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__方法类似于java中的toString方法
    def __str__(self):
        return '我的名字是{0},今年{1}岁了'.format(self.name, self.age)


stu = Student('张三', 20)
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
'''
print(dir(stu))
print(stu)
