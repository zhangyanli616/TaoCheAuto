# -*- coding:utf-8 -*-
from titan import tt_check
from taochePC import Base
from taochePC import HeaderLocator
from taochePC.config import config

url = config.home_url


class Header(Base):

    def test_logo(self):
        """测试顶通logo是否展示"""
        self.driver.get(url)
        logo_is_dispayed = self.driver.is_display(HeaderLocator.LOGO)

        tt_check.assertTrue(logo_is_dispayed, "首页Logo是否显示：%s" % logo_is_dispayed)

    def test_tchome(self):
        """测试顶通淘车首页链接跳转的正确性"""
        self.driver.get(url)
        self.driver.click(HeaderLocator.TC_HOME)
        url1 = self.driver.get_url()
        url2 = "https://www.taoche.com/"

        tt_check.assertEqual(url1, url2,
                             "测试顶通淘车首页的链接跳转， 期望是%s，实际是%s" % (url2, url1))

    def test_nav_menu(self):
        """测试首页导航显示是否正确"""
        navigation_expected = ["首页", "买车", "卖车", "分期", "资讯", "保险", "新车"]
        navigation_actual = []

        self.driver.get(url)
        navigation_bar = self.driver.find_element(HeaderLocator.NAV_MENU)
        navigation_links = navigation_bar.find_elements_by_tag_name('a')

        for navigation in navigation_links:
            navigation_actual.append(navigation.text)

        tt_check.assertEqual(navigation_actual, navigation_expected,
                             "导航期望是%s，实际是%s" % (navigation_expected, navigation_actual))

    def test_nav_default(self):
        """测试首页导航默认是否是首页"""
        self.driver.get(url)
        navigation_default = self.driver.find_element(HeaderLocator.NAV_DEFAULT)
        navigation_default_expected = "首页"
        navigation_default_actual = navigation_default.text

        tt_check.assertEqual(navigation_default_actual, navigation_default_expected,
                             "导航默认,期望为%s，实际为%s" % (navigation_default_expected, navigation_default_actual))
