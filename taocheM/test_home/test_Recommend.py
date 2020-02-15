# -*- coding:utf-8 -*-
#@author:xulanzhong

from titan import tt_check
from taocheM.base_m import Base
from taocheM.locator_m import Locator_Home
from taocheM.config_m import config

url = config.home_url

class Recommend(Base):

  def test_Recommend(self):

    """测试点击首页推荐楼层今日上新....，跳转新车是否包含新车签,@author:xulanzhong"""

    self.driver.get(url)

    self.driver.pause(2)

    self.driver.execute_script("window.scrollTo(0, 900)")

    self.driver.pause(2)

    self.driver.click(Locator_Home.Recommend)

    self.driver.pause(2)

    test_Recommend = self.driver.is_display(Locator_Home.today_new)

    tt_check.assertTrue(test_Recommend, "今日上新签是否显示， %s" % test_Recommend)


# def test_Newcar(self):
#     """测试默认品牌名称,@author:xulanzhong"""
#
#     Newcar_expect = ['新车推荐', '开走吧', '分期购车']
#
#     self.driver.get(url)
#
#     self.driver.execute_script("window.scrollTo(0, 900)")
#
#     self.driver.pause(2)
#
#     Newcar_li = self.driver.find_element(Locator_Home.Newcar_list)
#     Newcar_links = Newcar_li.find_elements_by_tag_name('a')
#
#     Newcar_actual = []
#
#     for Newcar_link in Newcar_links:
#         Newcar_actual.append(Newcar_link.text)
#
#     tt_check.assertEqual(sorted(Newcar_actual), sorted(Newcar_expect),
#                          "淘车新车楼层，期望是%s，实际是%s" % (Newcar_expect, Newcar_actual))

















# url = config.home_url
#
#
# def test_recommend(self):
#     """测试首页推荐楼层显示及跳转是否正确,@author:xulanzhong"""
#     self.driver.get(home_url)
#     price_li = self.driver.find_element(HomePageLocator.BUY_CAR_PRICE)
#     price_links = price_li.find_elements_by_tag_name('a')
#
#     # 遍历所有价格范围
#     result = []
#     for price_link in price_links:
#         try:
#             price = price_link.text
#             price_range = re.findall(r'\d+', price)
#             price_link.click()
#
#             # 在新窗口判断筛选条件是否为选择的价格范围
#             self.driver.switch_to_window()
#             self.driver.wait()
#
#             filter_content = self.driver.find_element(BuyCarLocator.FILTER_SELETED) \
#                 .find_element_by_tag_name('a').text
#             filter_price_range = re.findall(r'\d+', filter_content)
#             tt_check.assertEqual(price_range, filter_price_range,
#                                  "所选价格范围%s，跳转后已选择的筛选条件是%s" % (price, filter_content))
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