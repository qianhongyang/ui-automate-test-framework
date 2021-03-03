# -*- coding: utf-8 -*-


import pytest, time
from os.path import join
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.chrome.options import Options
from utils.operation_portal import portal_attachment
from utils.operation_path import get_picture_path
from utils.operation_log import Loggings
from utils.operation_profile import get_web_config, set_web_env
from utils.operation_picture import set_font_picture

driver = None


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
            set_font_picture(report.longreprtext, color=(242, 85, 0))
            if screen_img:
                portal_attachment(screen_img)


def _get_exception(report):
    print(report.longreprtext)


def _capture_screenshot():
    """截图私有方法"""
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    picture_name = "web-" + picture_time + ".png"
    mylogger().info("Screenshot save address:----> %s" % picture_name)
    picture_path = join(get_picture_path(), picture_name)
    driver.get_screenshot_as_file(picture_path)
    return picture_path


@pytest.fixture()
def web_driver(request):
    """返回driver，现在是Chrome"""
    global driver
    HEADLESS = get_web_config().get("HEADLESS")
    DEBUGGER = get_web_config().get("DEBUGGER")
    if HEADLESS is True:
        __options = Options()
        __options.add_argument('--headless')
        driver = WebChrome(chrome_options=__options)
    elif DEBUGGER is True:
        # 如果需要使用已经打开的，chrome浏览器的debugger模式，需要把以下三行代码释放
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = WebChrome(options=chrome_options)
    else:
        __options = Options()
        # 设置全屏
        __options.add_argument('--start-maximized')
        # 设置开发者模式
        __options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors",
                                                              "enable-automation"])
        driver = WebChrome(chrome_options=__options)

    yield driver
    driver.close()

    def end():
        driver.quit()

    request.addfinalizer(end)


def mylogger():
    """返回logger对象，引用log服务"""
    log = Loggings()
    return log


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="设置运行环境"
    )
    parser.addini("env", type="linelist", default="dev", help="设置自动化打开的浏览器访问网址--url 添加到 pytest 配置中")


@pytest.fixture(scope="session", autouse=True)
def env(pytestconfig):
    ENV = pytestconfig.getoption('--env')
    ENV.upper()
    set_web_env(ENV)
    mylogger().info("当前执行环境为：" + ENV)
    return ENV
