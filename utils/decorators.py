# -*- coding: utf-8 -*-

import inspect
import timeit
from functools import wraps
from collections import OrderedDict
import pytest, time
from os.path import join
from utils.operation_portal import portal_attachment
from utils.operation_path import get_picture_path
from utils.operation_log import Loggings

log = Loggings()
logger = log


def singleton(cls):
    """单例模式装饰器

    :param cls:
    :return:
    """
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


def singleton_with_parameters(cls):
    """检查参数的单例模式装饰器,与singleton的区别为: 相同的初始化参数为同一个实例

    :param cls:
    :return:
    """
    instances = {}

    def _singleton(*args, **kwargs):
        key = frozenset(inspect.getcallargs(cls.__init__, *args, **kwargs).items())
        if key not in instances:
            instances[key] = cls(*args, **kwargs)
        return instances[key]

    return _singleton


class SingletonIfSameParameters(type):
    """如果初始化参数一致，则单实例"""

    _instances = {}
    _init = {}

    def __init__(cls, name, bases, dct):
        cls._init[cls] = dct.get('__init__', None)

    def __call__(cls, *args, **kwargs):
        init = cls._init[cls]
        if init is not None:
            key = (cls, args, repr(OrderedDict(kwargs.items())))
        else:
            key = cls

        if key not in cls._instances:
            cls._instances[key] = super(SingletonIfSameParameters, cls).__call__(*args, **kwargs)
        return cls._instances[key]


class MaxRetriesExceeded(Exception):
    pass


def cached(func):
    """缓存装饰器,用于function,当传入参数一致,func不会再次执行,而是直接从缓存里取出上次执行结果返回

    :param func:
    :return:
    """
    cached_items = {}

    @wraps(func)
    def wrap(*args, **kwargs):
        key1 = "".join(map(lambda arg: str(id(arg)), args))
        key2 = OrderedDict(sorted({k: id(v) for k, v in kwargs.items()}.items()))
        key = key1 + "+" + str(key2)
        if key in cached_items:
            return cached_items[key]
        else:
            ret = func(*args, **kwargs)
            cached_items[key] = ret
            return ret

    return wrap


class Singleton:
    """单实例元类"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


def snapshot(driver):
    """该装饰器可以用于报错截图并上传到portal"""

    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except AssertionError:
                picture_path = _capture_screenshot(driver)
                portal_attachment(picture_path)
                raise AssertionError

        return _wrapper

    return wrapper


def _capture_screenshot(driver):
    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    picture_path = join(get_picture_path(), picture_time + ".png")
    driver.get_screenshot_as_file(picture_path)
    return picture_path


def snapshot_class(driver):
    """该装饰器可以用于报错截图并上传到portal"""

    def wrapper(cls):
        @wraps(cls)
        def _wrapper():
            try:
                for i in dir(cls):
                    if i.startswith("test"):
                        # eval("%s(self)" % i)
                        getattr(cls, i)()
            except AssertionError as msg:
                picture_path = _capture_screenshot(driver)
                portal_attachment(picture_path)
                raise (AssertionError, msg)

        return _wrapper

    return wrapper


def logger_doc(level="debug"):
    """该装饰器可以用于打印该函数doc为日志"""

    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            if level.lower() == "info":
                logger.info(func.__doc__)
            else:
                logger.debug(func.__doc__)
            return func(*args, **kwargs)

        return _wrapper

    return wrapper


def wait_element():
    """该装饰器可以用于元素等待"""

    def wrapper(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            for i in range(5):
                time.sleep(1)
                try:
                    return func(*args, **kwargs)
                except:
                    print("第%s次寻找元素~" % i)

        return _wrapper

    return wrapper
