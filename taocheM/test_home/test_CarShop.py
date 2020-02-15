# -*- coding:utf-8 -*-
#@author:xulanzhong
from titan import tt_check
from taocheM.base_m import Base
from taocheM.locator_m import Locator_Home
from taocheM.config_m import config


url = config.zhengzhou_url

class CarShop(Base):


    def test_CarShop(self):
        """测试郑州首页店铺显示正确性,@author:xulanzhong"""

        self.driver.get(url)

        self.driver.pause(1)

        self.driver.execute_script("window.scrollTo(0, 600)")

        self.driver.pause(2)

        self.driver.click(Locator_Home.carshop_click)

        self.driver.pause(2)

        test_carshop = self.driver.is_display(Locator_Home.carshop_name)

        tt_check.assertTrue(test_carshop, "店铺首页，是否显示 %s" % test_carshop)

