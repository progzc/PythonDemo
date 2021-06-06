# 多态

class Animal(object):
    def eat(self):
        print('动物要吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    @staticmethod
    def eat():
        print('人吃五谷杂粮')


def fun(animal):
    animal.eat()


fun(Dog())
fun(Cat())
fun(Person())
