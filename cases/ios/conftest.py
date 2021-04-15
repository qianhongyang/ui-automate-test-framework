# -*- coding: utf-8 -*-

import pytest, time
from os.path import join
from utils.operation_portal import portal_attachment
from utils.operation_path import get_picture_path
from utils.operation_log import Loggings
from utils.operation_profile import get_ios_config
from airtest.core.api import *
from poco.drivers.ios import iosPoco
from pages.app.ios.basePage import basePage

IosPoco = None
ADDRESS = get_ios_config().get("ADDRESS")  # 开放的wda服务端口


@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    """
    当测试失败的时候，钩子获取assert结果，如果失败会自动截图，详见pytest中outcome结果
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen_img = _capture_screenshot()
            if screen_img:
                portal_attachment(screen_img)


def _capture_screenshot():
    """截图私有方法"""
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    picture_name = "ios-" + picture_time + ".png"
    picture_path = join(get_picture_path(), picture_name)
    time.sleep(0.5)  # 这里如果不等待一秒时间会造成
    snapshot(filename=picture_path, msg="测试ios错误截图")
    mylogger().info("Screenshot save address:----> %s" % picture_name)
    return picture_path


@pytest.fixture(scope='function')
def ios_poco(request):
    global IosPoco
    if IosPoco is None:
        connect_device('iOS:///' + ADDRESS)
        IosPoco = iosPoco()
    yield IosPoco

    def end():
        home()

    request.addfinalizer(end)


def mylogger():
    """返回logger对象，引用log服务"""
    log = Loggings()
    return log


@pytest.fixture(scope="class")
def logger():
    return mylogger()
