# -*- coding: utf-8 -*-

import pytest
import yaml
from utils.operation_path import get_config_path


def _yaml_file():
    """
    获取yaml配置文件内容
    :return data(type:dict)
    """
    with open(get_config_path(), 'rb') as file:
        file_data = file.read()
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data


def get_log_config():
    """获取web的配置文件内容"""
    data = _yaml_file()
    return data.get("log")


def get_android_config():
    """获取Android的配置文件内容"""
    data = _yaml_file()
    return data.get("android")


def get_ios_config():
    """获取ios的配置文件内容"""
    data = _yaml_file()
    return data.get("ios")


def get_web_config():
    """获取web的配置文件内容"""
    data = _yaml_file()
    return data.get("web")


def get_portal_config():
    """获取portal的配置文件内容"""
    data = _yaml_file()
    return data.get("portal")


def get_web_data(project, option):
    """获取web对应环境的项目数据"""
    return get_web_env(project).get(option)


def get_web_env(project):
    """获取web_env的配置文件内容"""
    ENV = get_web_config().get("ENV").upper()

    if ENV == "DEV" or ENV == "PROD":
        return get_web_config().get(ENV).get(project)
    else:
        raise AttributeError("Incorrect ENV setting, select execution environment DEV or PROD!")


def set_web_env(env):
    """设置运行环境"""
    with open(get_config_path(), 'rb') as f:
        doc = yaml.safe_load(f)
    doc['web']['ENV'] = env.upper()
    with open(get_config_path(), 'w') as f:
        yaml.safe_dump(doc, f, default_flow_style=False)
