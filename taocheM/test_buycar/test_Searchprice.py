# -*- coding:utf-8 -*-
#@author:xulanzhong
from titan import tt_check
from taocheM.base_m import Base
from taocheM import locator_m
from taocheM.config_m import config

url = config.list_url


class searchprice(Base):

    def test_price(self):
        """测试列表页点击三万内价格条件，结果是否展示,@author:xulanzhong"""

        self.driver.get(url)

        self.driver.click(locator_m.Locator_BuyCar.price_click)

        self.driver.pause(2)

        price_is_dispayed = self.driver.is_display(locator_m.Locator_BuyCar.price_list)

        tt_check.assertTrue(price_is_dispayed, "是否显示：%s" % price_is_dispayed)

