# -*- coding: utf-8 -*-
from utils.android_connect_device import *
from utils.operation_profile import get_android_config
from pages.app.android.netease.main_page import MainPage


class TestMainSomething:
    """测试网易云主页一些东西"""

    def setup(self):
        self.PACKAGENAME = get_android_config().get("PACKAGENAME")

    def test_my_music(self, android_poco):
        """测试打开我的"""
        start_app(self.PACKAGENAME)
        main_page = MainPage(android_poco)
        sleep(10)
        main_page.my()
