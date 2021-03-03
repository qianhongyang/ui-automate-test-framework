# -*- coding: utf-8 -*-

from utils.operation_log import logger
from utils.operation_profile import get_web_data
from pages.web.baidu_page.baiduMainPage import baiduMainPage


class TestBaiduSearch:
    """测试百度搜索流程用例"""

    def setup(self):
        self.BAIDUURL = get_web_data("BAIDU", "BAIDUURL")

    def test_search_auto(self, web_driver):
        """测试百度auto结果流程"""
        logger.info(self.test_search_auto.__doc__)
        web_driver.get(self.BAIDUURL)
        baidu_main_page = baiduMainPage(web_driver, logger=logger)
        baidu_main_page.baidu_search_input("airtest")
        baidu_main_page.baidu_search_button()
        res = baidu_main_page.baidu_search_results().text
        assert "百度为您找到相关结果" in res


