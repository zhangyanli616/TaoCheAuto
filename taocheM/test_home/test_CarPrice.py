# -*- coding:utf-8 -*-
#@author:xulanzhong
from titan import tt_check
from taocheM.base_m import Base
from taocheM.locator_m import Locator_Home
from taocheM.config_m import config


url = config.home_url

class CarPrice(Base):


    def test_CarPrice(self):
        """测试首页价格糖豆,@author:xulanzhong"""

        price_expect = ['5万以下', '5-10万', '10-15万', '15万以上']

        self.driver.get(url)

        self.driver.execute_script("window.scrollTo(0, 300)")

        self.driver.pause(3)

        carprice_li = self.driver.find_element(Locator_Home.carprive_list)
        carprice_links = carprice_li.find_elements_by_tag_name('a')

        price_actual = []

        for carprice_link in carprice_links:
            price_actual.append(carprice_link.text)

        tt_check.assertEqual(sorted(price_actual), sorted(price_expect), "首页价格糖豆，期望价格是%s，实际是%s" % (price_expect, price_actual))


        self.driver.click(Locator_Home.carprive_click)


        test_price = self.driver.is_display(Locator_Home.carprive_foot)

        tt_check.assertTrue(test_price,"列表页筛选条件0-5万，是否显示 %s" % test_price)