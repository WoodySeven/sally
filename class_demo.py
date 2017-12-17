#!/usr/bin/env python


# 定义了一个Person类
class Person(object):
    population = 0  # 类变量,

    # 实例方法，初始化函数，必须写成  __init__()
    def __init__(self, name, age, address='yisilie'):
        Person.population += 1
        self.name = name  # 实例变量
        self.age = age
        addr = address   # 定义了一个局部变量而已

    # 实例方法，参数都用 self关键字，开头
    def say_hai(self):  # 实例方法
        # 实例变量
        print("{0} hello".format(self.name))

    @classmethod
    def how_many(cls): # 把实例方法，转变为类方法，使用装饰器
        print("Person population has {0}".format(Person.population))


class Man(Person):
    pass


yadang = Person("yadang", 18)
# 传统的调用函数的方式
# how_many(yadang)
yadang.say_hai()
Person.how_many()

xiawa = Person("xiawa", 16)
xiawa.say_hai()
Person.how_many()

# how_many(Person)
