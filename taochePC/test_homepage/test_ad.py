# -*- coding:utf-8 -*-
from titan import tt_check
from taochePC import Base
from taochePC.config import config
from taochePC import HomePageLocator

import requests


home_url = config.home_url


class AD(Base):

    def test_title(self):
        """测试首页Title显示是否正确"""
        self.driver.get(home_url)
        home_page_title_actual = self.driver.get_title()
        home_page_title_expected = "二手车市场_二手车交易市场_二手车平台-淘车网"

        tt_check.assertEqual(home_page_title_actual, home_page_title_expected,
                             "页面title期望是%s，实际是%s" % (home_page_title_expected, home_page_title_actual))

    def test_ad_displayed(self):
        """测试广告位图片请求是否正常"""
        self.driver.get(home_url)
        ads = self.driver.find_elements(HomePageLocator.FOCUS_PIC_IMG)

        ad_srcs = []
        for ad in ads:
            ad_src = ad.get_attribute('src')
            ad_srcs.append(ad_src)

        if not ad_srcs:
            raise Exception("未找到轮播广告图元素")

        # 遍历所有焦点图的src，查看访问是否正常
        result = []
        for ad_src in ad_srcs:
            try:
                ad_url_status = requests.get(ad_src).status_code
                tt_check.assertEqual(200, ad_url_status, "焦点图广告请求状态码，期望是200，实际是%d" % ad_url_status)

            except AssertionError as msg:
                result.append(msg)

        if result:
            raise AssertionError(result)

    # def test_ad_jump(self):
    #     """测试广告位跳转是否正常"""
    #     self.driver.get(home_url)
    #     ad_jump_elements = self.driver.find_elements(HomePageLocator.FOCUS_PIC_JUMP)
    #
    #     result = []
    #     for ad_jump_element in ad_jump_elements:
    #         try:
    #             if ad_jump_element.is_displayed():
    #                 ad_jump_element.click()  # 广告图轮播，点击时若不是当前广告，则会异常
    #                 self.driver.switch_to_window()
    #                 new_url = self.driver.get_url()
    #                 new_url_status = requests.get(new_url).status_code
    #
    #                 tt_check.assertEqual(200, new_url_status, "焦点图广告跳转后页面状态，期望是200，实际是%d" % new_url_status)
    #
    #         except AssertionError as msg:
    #             result.append(msg)
    #
    #         finally:
    #             # 重置driver
    #             self.driver.switch_to_window()
    #             self.driver.close_other_window()
    #
    #     if result:
    #         raise AssertionError(result)

