from utils.android_connect_device import *


class Test:
    """测试（基于联系人页面。点击到拨打号码，出来弹窗即可）"""

    def test_call(self, android_poco):
        """中转号测试"""
        start_app()
        self.page = ContactPage(android_poco)
        self.page.home_CRM_button()
        self.page.crm_firm_button()
        self.page.search_contact('test')
        self.page.firm_contact_button()
        self.page.contact_info_button()
        self.page.contact_call_button()  # 点击拨打电话，弹出弹窗“查看联系方式”

        assert android_poco('查看联系方式').exists()
        self.page.contact_call_confirm_button()  # 拨打后返回校验是否到联系人页面

        assert android_poco('公司').exists()
        self.page.contact_homepage_button()
