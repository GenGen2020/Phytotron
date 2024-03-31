#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/31 9:33
# @Author  : 晚秋
# @File    : validate.py
# @Description : 文件作用注释
from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # 获取文件扩展名
    valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')
