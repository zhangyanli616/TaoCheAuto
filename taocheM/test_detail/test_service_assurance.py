# -*- coding:utf-8 -*-
from titan import tt_check
from taocheM.base_m import Base
from taocheM.config_m import TestConfig
from taocheM.locator_m import CarDetail_Locator
from time import sleep
from titan.tt_log import LOG
from titan import SeleniumDriver

service_assurance_url=TestConfig.service_url

# 详情页点击『服务保障』检查

class Service(Base):
    def test_service_title(self):
        """测试服务保障页title显示的是否正确@author:zhangyanli"""
        self.driver.get(service_assurance_url)
        service_title = self.driver.find_element(CarDetail_Locator.SEVICE_TITLE).text
        tt_check.assertEqual("保真车保真标准说明", service_title, "服务保障页的title，期望是保真车保真标准说明，实际是%s" % service_title)