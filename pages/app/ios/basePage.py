# -*- coding: utf-8 -*-


class basePage:
    """
    所有pages的基类，所有的剩余page应该继承Page类
    """

    def __init__(self, poco):
        self.poco = poco
