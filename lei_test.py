#  -*- coding:UTF-8 -*-
class Man(object):                                          #class 类名（object或如果是一个子类，就填个父类）
    def __init__(self, name, age):                          #初始化（self, 属性）
        self.name = name                                    #self.属性 = 属性
        self.age = age

    def print_man(self):
        print 'name =%s,age =%s' % (self.name,self.age)

zs = Man('zhangsan', 18)                                    #实例 = 方法（给各属性一个真正的例子）
Man.print_man(zs)                                           #调用类里面的一个方法，用类名.方法（实例）
print zs.age