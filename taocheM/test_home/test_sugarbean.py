# -*- coding:utf-8 -*-
#@author:xulanzhong
from titan import tt_check
from taocheM.base_m import Base
from taocheM.locator_m import Locator_Home
from taocheM.config_m import config

url = config.home_url


class SugarBean(Base):

    # def test_sugarbean(self):
    #     """测试糖豆名是否正确,@author:xulanzhong"""
    #
    #     sugar_except = ["买二手车","全国购","超低月供","分期购","准新车","热销SUV","估价","练手车","明星车","新车"]
    #
    #     self.driver.get(url)
    #
    #     self.driver.pause(3)
    #
    #     self.driver.click(Locator_Home.flush__click)
    #
    #     sugar_li = self.driver.find_element(Locator_Home.sugar_list)
    #     sugar_links = sugar_li.find_elements_by_tag_name('li')
    #
    #     sugar_actual = []
    #
    #     for sugar_link in sugar_links:
    #         sugar_actual.append(sugar_link.text)
    #
    #
    #     tt_check.assertEqual(sorted(sugar_actual),sorted(sugar_except),"首页糖豆期望是%s,实际是%s" % (sugar_except,sugar_actual))

    def test_qgg(self):

        """测试全国购跳转是否正确，首页并显示足迹"""
        self.driver.get(url)

        self.driver.pause(2)

        self.driver.click(Locator_Home.flush_click)

        self.driver.pause(2)

        #self.driver.click(Locator_Home.sugar_qgg)

        test_qgg = self.driver.is_display(Locator_Home.test_qgg)

        tt_check.assertTrue(test_qgg,"列表页命中条件，是否显示: %s" % test_qgg)

        # self.driver.pause(2)
        #
        # self.driver.back()
        #
        # test_foot = self.driver.is_display(Locator_Home.test_footstep)
        #
        # tt_check.assertTrue(test_foot,"首页足迹是否显示：%s" % test_foot)















# import time
#
# from taocheM.base_m import Base
# from taocheM.config_m import config
# from taocheM.locator_m import locator_sugar_bean
#
# home_url = config.home_url
#
#
# class HomePage(Base):
#     pass
#
#     def test_sugar_bean(self):
#         self.driver.get(home_url)
#         time.sleep(2)
#         DIV_SHOW=self.driver.find_element(locator_sugar_bean.DIV_CLASS)
#         if DIV_SHOW:
#             self.driver.find_element(locator_sugar_bean.CLOSE_DIV_GATE).click()
#         else:
#             pass
#
#         sugarBeanList = self.driver.find_element(locator_sugar_bean.SUGAR_BEAN).find_elements_by_tag_name('li')
#         for sugarBean in sugarBeanList:
#             sugarBeanText = sugarBean.text
#             print(sugarBeanText)
#             sugarBeanURL = sugarBean.find_element_by_tag_name('a').get_attribute('href')
#             print(sugarBeanURL)
