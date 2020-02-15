# # -*- coding:utf-8 -*-
# #@author:xulanzhong
# from titan import tt_check
# from taocheM.base_m import Base
# from taocheM.locator_m import Locator_Home
# from taocheM.config_m import config
# import requests
#
# url = config.home_url
#
# class topic(Base):
#
#  def test_topic(self):
#     """测试广告位图片请求是否正常"""
#     self.driver.get(url)
#     ads = self.driver.find_elements(Locator_Home.topic)
#
#     ad_srcs = []
#     for ad in ads:
#         ad_src = ad.get_attribute('src')
#         ad_srcs.append(ad_src)
#
#     if not ad_srcs:
#         raise Exception("未找到轮播广告图元素")
#
#     # 遍历所有焦点图的src，查看访问是否正常
#     result = []
#     for ad_src in ad_srcs:
#         try:
#             ad_url_status = requests.get(ad_src).status_code
#             tt_check.assertEqual(200, ad_url_status, "焦点图广告请求状态码，期望是200，实际是%d" % ad_url_status)
#
#         except AssertionError as msg:
#             result.append(msg)
#
#     if result:
#         raise AssertionError(result)