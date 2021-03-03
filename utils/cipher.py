# -*- coding: utf-8 -*-

import hashlib


def encryption(pw, salt='rcc_test'):
    """加密password"""
    new_s = str(pw) + salt
    m = hashlib.md5(new_s.encode())
    return m.hexdigest()


