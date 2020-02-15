# -*- coding:utf-8 -*-
#@author:xulanzhong

from titan import tt_check
from taocheM.base_m import Base
from taocheM.locator_m import Locator_Home
from taocheM.config_m import config


url = config.home_url

class Hotsearch(Base):

    def test_Hotsearch(self):
        """测试首页搜索,@author:xulanzhong"""

        self.driver.get(url)

        self.driver.pause(2)

        self.driver.click(Locator_Home.search)

        self.driver.pause(2)

        self.driver.click(Locator_Home.bzcar)

        test_bzcar = self.driver.is_display(Locator_Home.bzcar_foot)

        tt_check.assertTrue(test_bzcar,"列表页筛选条件保真车，是否显示 %s" % test_bzcar)


