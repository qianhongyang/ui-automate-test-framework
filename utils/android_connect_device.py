# -*- coding: utf-8 -*-
import subprocess
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from utils.operation_profile import get_android_config

ADDRESS = get_android_config().get("ADDRESS")  # 获取config.yml中ADDRESS


def android_get_devices():
    """用于获取当前连接机器"""
    # 获取andriod设备id的command
    command_get_devices = "adb devices|grep -w 'device'|awk -F ' ' '{print $1}'"
    my_device = subprocess.getoutput(command_get_devices)
    command_get_devices_num = "adb devices|grep -w 'device'|awk -F ' ' '{print $1}'| wc -l"
    my_device_number = int(subprocess.getoutput(command_get_devices_num).strip())
    if my_device_number > 1:
        raise OSError("存在多个Android设备！")
    elif my_device_number < 1:
        raise OSError("没有连接的Android!")
    return my_device


def android_connet(my_phone):
    """用于连接安卓设备的方法，需要判断是否已经连接，如果设备已经通过poco库连接的情况下，那么就不能重新返回poco实例"""
    try:

        my_device_driver = connect_device(ADDRESS + my_phone)
        poco = AndroidUiautomationPoco(my_device_driver, force_restart=False)
        return poco
    except Exception as e:
        print("\033[7;31m%s\033[1;31;40m" % e)


def android_kill():
    """用于断开当前设备连接"""
    command = "adb kill-server"
    my_device = subprocess.getoutput(command)
    print(my_device)


def android_start():
    """用于当前设备连接"""
    command = "adb start-server"
    my_device = subprocess.getoutput(command)
    print(my_device)
