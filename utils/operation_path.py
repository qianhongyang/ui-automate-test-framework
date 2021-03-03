# -*- coding: utf-8 -*-

import sys, os


def get_system_info():
    """获取系统类型"""
    system = sys.platform

    if system == "darwin" or system == "linux":
        symbol = "/"
    else:
        symbol = "\\"
    return symbol


def get_projrct_root_dir():
    """获取项目根目录"""
    full_path = __file__
    symbol = get_system_info()
    list_path = full_path.split(symbol)

    if "ui-automate-test-framework" in list_path:
        index = list_path.index("ui-automate-test-framework")
        root_dir = "/".join(list_path[:index + 1])
        return root_dir
    else:
        return None


def get_config_path():
    """获取配置文件绝对路径"""
    root_dir = get_projrct_root_dir()
    return os.path.join(root_dir, "config", "config.yml")


def get_log_path():
    """获取log文件绝对路径"""
    root_dir = get_projrct_root_dir()
    log_path = os.path.join(root_dir, "log")
    log_path_file = os.path.join(log_path, "run_log.log")
    if os.path.exists(log_path_file) is False:
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
        if not os.path.isfile(log_path_file):  # 无文件时创建
            fd = open(log_path_file, mode="w", encoding="utf-8")
            fd.close()
    return log_path_file


def get_picture_path():
    """获取picture文件绝对路径"""
    root_dir = get_projrct_root_dir()
    picture_path = os.path.join(root_dir, "reports", "picture")
    if not os.path.isdir(picture_path):
        os.makedirs(picture_path)
    return picture_path


def get_font_path():
    """获取ttf文件绝对路径"""
    root_dir = get_projrct_root_dir()
    font_path = os.path.join(root_dir, "assets", "font")
    if not os.path.isdir(font_path):
        os.makedirs(font_path)
    return font_path


def get_images_path():
    """获取图像识别文件绝对路径"""
    root_dir = get_projrct_root_dir()
    images_path = os.path.join(root_dir, "assets", "images")
    return images_path
