# -*- coding:utf-8 -*-
from titan import tt_check
from taocheM.base_m import Base
from taocheM.config_m import TestConfig
from taocheM.locator_m import CarDetail_Locator
from time import sleep
from titan.tt_log import LOG
from titan import SeleniumDriver


detail_url = 'https://m.taoche.com/buycar/b-dealermd233736134t.html'

# 详情页点击『检测报告』检查

class Report(Base):
    def test_report_title(self):
        """测试检测报告title显示的是否正确@author:zhangyanli"""
        self.driver.get(detail_url)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1300)")
        report_title = self.driver.find_element(CarDetail_Locator.REPORT_TITLE).text
        tt_check.assertEqual("检测报告", report_title, "检测报告tab的title，期望是检测报告，实际是%s" % report_title)

    def test_report_type(self):
        """测试检测报告各类型显示的是否正确@author:zhangyanli"""
        self.driver.get(detail_url)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1300)")
        report_type = self.driver.find_element(CarDetail_Locator.REPORT_TYPE).find_elements_by_class_name('display-flex')
        # for i in range(len(report_type)):
        #     LOG.info(report_type[i].text)
        for i in range(len(report_type)):
            config_value = report_type[i].find_elements_by_tag_name('div')
            keyval = ""
            for j in range(len(config_value)):
                yu = j % 2
                if(yu == 0):
                    keyval = config_value[j].text

                else:
                    keyval = keyval + ":" + config_value[j].text
                    print(keyval)
                    keyval = ""







