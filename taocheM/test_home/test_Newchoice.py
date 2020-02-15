# # -*- coding:utf-8 -*-
# #@author:xulanzhong
# from titan import tt_check
# from taocheM.base_m import Base
# from taocheM import locator_m
# from taocheM.config_m import config
#
# url = config.home_url
#
#
# class Newchoice(Base):
#
#     def test_Newchoice(self):
#         """测试首页淘车心选楼层是否展示,@author:xulanzhong"""
#         self.driver.get(url)
#
#         self.driver.set_window_size(100, 100,)
#
#         self.driver.pause(2)
#
#         self.driver.execute_script("window.scrollTo(0, 900)")
#
#         self.driver.pause(2)
#
#         Newchoice_is_dispayed = self.driver.is_display(locator_m.Locator_Home.Newchoice)
#
#         self.driver.pause(3)
#
#         tt_check.assertTrue(Newchoice_is_dispayed, "首页淘车心选是否显示：%s" % Newchoice_is_dispayed)
#
#
#
#
