# -*- coding: utf-8 -*-

import os
from PIL import Image, ImageDraw, ImageFont
from utils.operation_path import get_picture_path, get_system_info, get_font_path

picture_dir_path = get_picture_path()


def get_new_picture():
    """获取最新的图片"""
    files = os.listdir(picture_dir_path)
    lists = []  # 列出目录的下所有文件和文件夹保存到lists
    for f in files:
        if f.startswith("web"):
            lists.append(f)

    lists.sort(key=lambda fn: os.path.getmtime(picture_dir_path + "/" + fn))  # 按时间排序
    file_new = os.path.join(picture_dir_path, lists[-1])  # 获取最新的文件保存到file_new
    return file_new


def get_picture_info(picture_path):
    """
    获取图片信息
    format:获取图片格式,类型: string or None
    mode:图片模式。图片使用的像素格式，典型的格式有 “1”, “L”, “RGB”, or “CMYK.” * 类型: string
    size:图片尺寸（以像素为单位）类型: (width, height)
    width:图片像素宽 类型: int
    height:图片像素高 类型: int
    palette:调色板。如果模式是“P”，则是一个ImagePalette类的实例。 类型: ImagePalette or None
    info:一个与图片有关的数据组成的字典 类型: dict
    """
    im = Image.open(picture_path)
    return im


def set_font_picture(text, color):
    picture_path = get_new_picture()
    image = Image.open(picture_path)
    draw = ImageDraw.Draw(image)
    font_path = os.path.join(get_font_path(), "FiraMono-Regular.ttf")
    font = ImageFont.truetype(font_path, 50)
    # 显示图片
    draw.text((100, 100), text, font=font, fill=color, stroke_width=15, stroke_fill=(249, 205, 173))
    # 保存
    # picture_name = picture_path.split(get_system_info())[-1]
    image.save(picture_path)
