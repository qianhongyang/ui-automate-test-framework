from time import sleep
from utils.decorators import logger_doc
from pages.app.ios.basePage import basePage


class MainPage(basePage):
    """网易云主页类"""

    @logger_doc()
    def my(self):
        """主页-我的"""
        return self.poco("我的").click()
