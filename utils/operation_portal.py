# -*- coding: utf-8 -*-

import os
import subprocess
import traceback
from mimetypes import guess_type
from time import time
from utils.operation_profile import get_portal_config

from reportportal_client import ReportPortalServiceAsync
from pytest_reportportal.service import PyTestServiceClass


def timestamp():
    return str(int(time() * 1000))


class PortalService:

    def __init__(self, portal_launch_name, portal_launch_doc):
        # Report Portal versions below 5.0.0:

        self.endpoint = get_portal_config().get("ENDPOINT")  # portal服务地址
        self.project = get_portal_config().get("PROJECT")  # portal项目名称
        self.token = get_portal_config().get("TOKEN")  # portal token

        self.service = ReportPortalServiceAsync(endpoint=self.endpoint, project=self.project,
                                                token=self.token, error_handler=self.my_error_handler)

        # Start launch.
        self.launch = self.service.start_launch(name=portal_launch_name,
                                                start_time=timestamp(),
                                                description=portal_launch_doc)

        # Start test item Report Portal versions below 5.0.0:
        self.test = self.service.start_test_item(name="Test Case",
                                                 description="First Test Case",
                                                 tags=["Image", "Smoke"],
                                                 start_time=timestamp(),
                                                 item_type="STEP",
                                                 parameters={"key1": "val1",
                                                             "key2": "val2"})

        self.service.finish_test_item(end_time=timestamp(), status="PASSED")
        # Finish launch.
        self.service.finish_launch(end_time=timestamp())
        self.service.terminate()

    @staticmethod
    def my_error_handler(exc_info):
        """
        This callback function will be called by async service client when error occurs.
        Return True if error is not critical and you want to continue module_2.
        :param exc_info: result of sys.exc_info() -> (type, value, traceback)
        :return:
        """
        print("Error occurred: {}".format(exc_info[1]))
        traceback.print_exception(*exc_info)

    def service_text_message(self):
        # Create text log message with INFO level.
        self.service.log(time=timestamp(),
                         message="Hello World!",
                         level="INFO")

    def service_message_with_attached_text(self):
        # Create log message with attached text output and WARN level.
        self.service.log(time=timestamp(),
                         message="Too high memory usage!",
                         level="WARN",
                         attachment={
                             "name": "free_memory.txt",
                             "data": "subprocess.check_output('free -h'.split())",
                             "mime": "text/plain"
                         })

    def service_message_with_image(self):
        # Create log message with binary file, INFO level and custom mimetype.
        image = "./image.png"
        with open(image, "rb") as fh:
            attachment = {
                "name": os.path.basename(image),
                "data": fh.read(),
                "mime": guess_type(image)[0] or "application/octet-stream"
            }
            self.service.log(timestamp(), "Screen shot of issue.", "INFO", attachment)

    def service_message_with_command_line(self):
        # Create log message supplying only contents
        self.service.log(
            timestamp(),
            "running processes",
            "INFO",
            attachment=subprocess.check_output("ps aux".split()))


def portal_attachment(file_path, msg="Screen shot of issue ------>"):
    """带附件的信息发送给portal"""
    rp = PyTestServiceClass()
    file = file_path
    with open(file, "rb") as fh:
        attachment = {
            "name": os.path.basename(file),
            "data": fh.read(),
            "mime": "application/octet-stream"
        }
    rp.post_log(msg, "INFO", attachment)
