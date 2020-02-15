# -*- coding:utf-8 -*-
from titan import tt_check
from taochePC import Base
from taochePC.config import config
from taochePC import HomePageLocator
from taochePC import HeaderLocator


home_url = config.home_url


class SellCar(Base):

    def test_sellcar_title(self):
        """测试我要卖车区域Title显示的是否正确"""
        self.driver.get(home_url)
        sellcar_title = self.driver.find_element(HomePageLocator.SELL_CAR_TITLE).text

        tt_check.assertEqual("我要卖车", sellcar_title, "我要卖车区域的title，期望是我要卖车，实际是%s" % sellcar_title)

    def test_sellcar_jump(self):
        """测试我要卖车区域title跳转"""
        self.driver.get(home_url)
        self.driver.click(HomePageLocator.SELL_CAR_TITLE)
        nav_sellcar_class = self.driver.find_element(HeaderLocator.NAV_SELLCAR).get_attribute('class')

        tt_check.assertEqual('current', nav_sellcar_class, "测试点击我要卖车title，跳转后的页面导航卖车是否为选中状态")

    def test_sellcar_submit(self):
        """测试我要卖车区域title跳转"""
        self.driver.get(home_url)
        self.driver.click(HomePageLocator.SELL_CAR_SUBMIT)
        nav_sellcar_class = self.driver.find_element(HeaderLocator.NAV_SELLCAR).get_attribute('class')

        tt_check.assertEqual('current', nav_sellcar_class, "测试点击我要卖车按钮，跳转后的页面导航卖车是否为选中状态")

    def test_sellcar_pinggu_nophone(self):
        """测试我要卖车区域不输入电话号码时免费评估submit跳转"""
        self.driver.get(home_url)
        self.driver.click(HomePageLocator.SELL_CAR_PINGU)

        url_actual = self.driver.get_url()
        url_expected = Config.pinggu_url

        tt_check.assertEqual(url_actual, url_expected, "测试点击免费评估按钮，跳转后的页面是否为评估url")

    def test_sellcar_pinggu_phone(self):
        """测试我要卖车区域输入电话号码时免费评估submit跳转"""
        self.driver.get(home_url)
        phone = '13000000000'
        self.driver.send_keys(HomePageLocator.SELL_CAR_PHONE, phone)
        self.driver.click(HomePageLocator.SELL_CAR_PINGU)

        url_actual = self.driver.get_url()
        url_expected = Config.pinggu_url + '?phone=' + phone

        tt_check.assertEqual(url_actual, url_expected, "测试输入手机号点击免费评估按钮，跳转后的页面地址是否包含手机号")

