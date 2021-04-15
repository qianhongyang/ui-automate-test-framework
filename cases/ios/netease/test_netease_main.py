# -*- coding: utf-8 -*-

from airtest.core.api import start_app
from time import sleep
from utils.operation_profile import get_ios_config
from pages.app.ios.netease.main_page import MainPage


class TestNeteaseMainPage:
    """测试主页的一些东西"""

    def setup(self):
        self.PACKAGENAME = get_ios_config().get("PACKAGENAME")

    def test_my(self, ios_poco):
        """ 测试'我的' """
        start_app(self.PACKAGENAME)
        self.page = MainPage(ios_poco)
        self.page.my()
        assert self.page.poco("立即登录")
