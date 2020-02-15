# -*- coding:utf-8 -*-
import select
import time
import requests
from django.forms import Select

from taochePC.config import config
from taochePC import Base, BuyCarLocator,HomePageLocator
from titan import tt_check, LOG

pinggu_url = config.pinggu_url

class Evaluation(Base):
    def test_evaluation(self):
        """验证估价页面，选择某辆车进行估价，得到估计结果@author:gaoxinling"""
        #打开评估页面
        self.driver.get(pinggu_url)
        time.sleep(2)
        #刷新页面获取默认城市
        self.driver.F5()
        time.sleep(1)
        #选择品牌和车系
        brand =self.driver.find_element(HomePageLocator.SELL_CAR_input).click()
        time.sleep(1)
        audi_brand = self.driver.find_element(HomePageLocator.AUDI_BRAND).click()
        time.sleep(1)
        yiqi_ser =self.driver.find_element(HomePageLocator.AUDI100_SER).click()
        time.sleep(2)
        #pList = self.driver.find_elements(HomePageLocator.VEHICLE_SEL)
        #选择车款
        classList = self.driver.find_element(HomePageLocator.SERIAL_DIR_ID).find_elements_by_class_name('form-popover-p')
        pList = classList[0].find_elements_by_tag_name('p')
        aText1 = pList[0].find_element_by_tag_name('a').text
        aText = pList[0].find_element_by_tag_name('a').click()
        #选择上牌时间：
        self.driver.find_element(HomePageLocator.license_plate).click()
        #time.sleep(1)
        self.driver.find_element(HomePageLocator.license_plate_year).click()
        #time.sleep(1)
        self.driver.find_element(HomePageLocator.license_plate_mounth).click()
        #输入里程
        a = self.driver.find_element(HomePageLocator.mileage).send_keys(2)
        #输入手机号
        self.driver.find_element(HomePageLocator.telephone_input).send_keys(18712341234)
        #点击开始估价
        #time.sleep(2)
        self.driver.find_element(HomePageLocator.evaluate_sell).click()
        #跳转新页面（估价结果页）
        self.driver.switch_to_window()
        #结果页取相应信息
        price1 = self.driver.find_element(HomePageLocator.price1).text
        price2 = self.driver.find_element(HomePageLocator.price2).text
        price3 = self.driver.find_element(HomePageLocator.price3).text
        print(aText1 +':车况一般的价格是' +price1)
        print(aText1 + ':正常磨损的价格是' + price2)
        print(aText1 + ':车况优秀的的价格是' + price3)
        LOG.info("【测试通过】")



