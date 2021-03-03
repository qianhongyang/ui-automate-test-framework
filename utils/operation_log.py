# -*- coding: utf-8 -*-

from loguru import logger
from utils.operation_profile import get_log_config
from utils.operation_path import get_log_path


class Loggings:
    __instance = None
    LEVEL = get_log_config().get("LEVEL")
    ROTATION = get_log_config().get("ROTATION")
    logger.add(get_log_path(), level=LEVEL, rotation=ROTATION)

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)
