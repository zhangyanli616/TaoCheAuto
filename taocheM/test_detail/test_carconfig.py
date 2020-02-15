# -*- coding:utf-8 -*-
from titan import tt_check
from taocheM.base_m import Base
from taocheM.config_m import TestConfig
from taocheM.locator_m import CarDetail_Locator
from time import sleep
from titan.tt_log import LOG
from titan import SeleniumDriver


carconfig_url = TestConfig.carconfig_url

# 详情页点击『参数配置』检查

class Config(Base):
    def test_config_title(self):
        """测试参数配置页title显示的是否正确@author:zhangyanli"""
        self.driver.get(carconfig_url)
        config_title = self.driver.find_element(CarDetail_Locator.CONFIG_TITLE).text
        tt_check.assertEqual("参数分配", config_title, "参数配置页的title，期望是参数分配，实际是%s" % config_title)

    def test_config_category(self):
        """测试参数配置信息显示的是否正确@author:zhangyanli"""
        self.driver.get(carconfig_url)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")
        config_list = self.driver.find_element(CarDetail_Locator.CONFIG_SIZE).find_elements_by_class_name('c-txt')
        for i in range(len(config_list)):
            config_value = config_list[i].find_elements_by_tag_name('span')
            keyval = ""
            for j in range(len(config_value)):
                yu = j % 2
                if(yu == 0):
                    keyval = config_value[j].text

                else:
                    keyval = keyval + ":" + config_value[j].text
                    print(keyval)
                    keyval = ""


