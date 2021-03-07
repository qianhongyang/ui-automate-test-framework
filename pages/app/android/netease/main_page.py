# -*- coding: utf-8 -*-
from time import sleep
from utils.decorators import logger_doc
from pages.app.android.basePage import basePage


class MainPage(basePage):
    """网易云主页类"""

    def __init__(self, poco):
        basePage.__init__(self, poco)

    @logger_doc()
    def my(self):
        """主页-我的"""
        return self.poco("android.widget.LinearLayout").offspring("com.netease.cloudmusic:id/bottomNav").child(
            "android.view.ViewGroup")[2].click()
