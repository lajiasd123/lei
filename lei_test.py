class Man(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_man(self):
        print 'name =%s,age =%s' % (self.name,self.age)

zs = Man('zhangsan', 18)
Man.print_man(zs)