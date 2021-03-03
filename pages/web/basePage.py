# -*- coding: utf-8 -*-
from utils.operation_profile import get_web_env, get_web_config
from utils.operation_log import logger
from utils.operation_profile import set_web_env
from utils.decorators import wait_element
import time
from os.path import join
from utils.operation_path import get_picture_path
from utils.operation_portal import portal_attachment


class basePage:
    """
    所有pages的基类，所有的剩余page应该继承Page类
    logger是否开启logger属性，默认不开启，在cases编写时，多个Page类继承此类时，
    只需要在一个case文件中一个Page类实例开启日志调用即可，否则会出现写入日志内容重复
    """

    def __init__(self, driver):
        self.driver = driver

    def _capture_screenshot(self):
        """截图方法"""
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        picture_name = "web-" + picture_time + ".png"
        logger.info("Screenshot save address:----> %s" % picture_name)
        picture_path = join(get_picture_path(), picture_name)
        self.driver.get_screenshot_as_file(picture_path)
        return picture_path

    def screen(self, doc):
        picture_path = self._capture_screenshot()
        portal_attachment(picture_path, msg=doc)
        return picture_path

    def _apply_style(self, element):
        """The screenshot identifies the element until"""
        js = "arguments[0].style.border='3px solid red'"
        self.driver.execute_script(js, element)

    @wait_element()
    def find_element(self, *args):
        element = self.driver.find_element(*args)
        if element:
            self._apply_style(element)
            return element

    @wait_element()
    def find_element_by_id(self, *args):
        element = self.driver.find_element_by_id(*args)
        if element:
            self._apply_style(element)
            return element

    @wait_element()
    def find_element_by_xpath(self, *args):
        element = self.driver.find_element_by_xpath(*args)
        if element:
            self._apply_style(element)
            return element

    @wait_element()
    def find_elements_by_xpath(self, *args):
        element = self.driver.find_elements_by_xpath(*args)
        if element:
            self._apply_style(element)
            return element

    @wait_element()
    def find_element_by_link_text(self, text):
        element = self.driver.find_element_by_link_text(text)
        if element:
            self._apply_style(element)
            return element

    @wait_element()
    def body_text(self, name="body"):
        element = self.driver.find_element_by_tag_name(name)
        if element:
            self._apply_style(element)
            return element

    def assert_equal(self, data, dev_data, prod_data):
        """根据环境断言是否相等"""
        if self.env == "DEV":
            assert data == dev_data
        elif self.env == "PROD":
            assert data == prod_data

    def find_element_exist_by_xpath(self, element):
        """如果元素存在则返回True，不存在返回False"""
        is_element = True
        try:
            self.driver.find_element_by_xpath(element)
        except Exception as e:
            print(e)
            is_element = False
        return is_element
