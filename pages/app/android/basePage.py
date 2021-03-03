# -*- coding: utf-8 -*-
from utils.operation_log import logger
from utils.decorators import wait_element
from airtest.core.api import keyevent
from time import sleep


class basePage:
    """
    所有pages的基类，所有的剩余page应该继承Page类
    """

    def __init__(self, poco):
        self.logger = logger
        self.poco = poco

    def back_homepage(self, ele_name='scan_code'):
        """
        APP测试每次用例执行后返回首页
        """
        # 最多10次迭代
        for i in range(10):
            # 判断是否返回了首页（首页特有元素判断）,没有返回首页点击返回键，返回了首页循环退出
            if not self.poco(ele_name).exists():
                keyevent("KEYCODE_BACK")
            else:
                break

    def poco_text(self, text):
        for i in range(20):
            sleep(0.5)
            element = self.poco(text)
            if element:
                return element
