# -*- coding: utf-8 -*-

from pages.web.basePage import basePage


class baiduMainPage(basePage):
    """百度主界面"""

    def __init__(self, driver, logger):
        basePage.__init__(self, driver)
        self.logger = logger

    def baidu_search_input(self, parms):
        """这是百度的输入框"""
        self.screen(doc=self.baidu_search_input.__doc__)
        self.logger.debug(self.baidu_search_input.__doc__)
        return self.find_element_by_xpath('//*[@id="kw"]').send_keys(parms)

    def baidu_search_button(self):
        """这是百度主页的搜索按钮"""
        self.screen(doc=self.baidu_search_button.__doc__)
        self.logger.debug(self.baidu_search_button.__doc__)
        return self.find_element_by_xpath('//*[@id="su"]').click()

    def baidu_search_results(self):
        """结果页面"""
        self.screen(doc=self.baidu_search_results.__doc__)
        self.logger.debug(self.baidu_search_results.__doc__)
        return self.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/span')

    def retrun_main_page(self):
        """返回首页"""
        self.screen(doc=self.retrun_main_page.__doc__)
        self.logger.debug(self.retrun_main_page.__doc__)
        return self.find_element_by_xpath('/html/body/div/header/div/div/div[5]/a').click()

    def some_element(self):
        return self.find_element_by_xpath('//*[@id="sh_1"]').click()
