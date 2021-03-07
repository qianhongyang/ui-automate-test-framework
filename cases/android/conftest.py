# -*- coding: utf-8 -*-

import pytest, time
from os.path import join
from airtest.core.api import *
from utils.operation_portal import portal_attachment
from utils.operation_path import get_picture_path
from utils.operation_log import Loggings
from utils.android_connect_device import android_start, android_get_devices, android_connet
from pages.app.android.basePage import basePage

AdroidPoco = None


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
            # 报错的地方截图之后返回到首页
            page = basePage(AdroidPoco)
            page.back_homepage()


def _capture_screenshot():
    """截图私有方法"""
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    picture_name = "android-" + picture_time + ".png"
    picture_path = join(get_picture_path(), picture_name)
    time.sleep(0.75)  # 这里如果不等待时间会造成截图黑屏，因为可能截到它切换时画面
    snapshot(filename=picture_path)
    mylogger().info("Screenshot save address:----> %s" % picture_name)
    return picture_path


@pytest.fixture(scope="module")
def android_poco(request):
    """注意，如果确定设备已经连接且驱动总是nonetype报错，可能为adb在电脑上无执行权限"""
    global AdroidPoco
    if AdroidPoco is None:
        android_start()
        my_device = android_get_devices()
        init_device(uuid=my_device)
        AdroidPoco = android_connet(my_device)
    yield AdroidPoco

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
