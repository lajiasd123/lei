# -×- coding:UTF-8 -*-
class Enemy(object):
    def __init__(self, leixing, hp):
        self.leixing = leixing
        self.hp = hp

class Map(object):
    def __init__(self, dixing):
        self.dixing = dixing

class Room(Map):
    pass

class outside(Map):
    pass

class yao(object):
    pass

class yao_lv(yao):
    pass

class yao_lan(yao):
    pass

class Attack(object):
    pass

class Hero(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        self.name = raw_input("请输入你英雄的名字/n:>>>")
        return Map