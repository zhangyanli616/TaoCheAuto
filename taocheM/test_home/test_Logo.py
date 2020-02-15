# -*- coding:utf-8 -*-
#@author:xulanzhong
from titan import tt_check
from taocheM.base_m import Base
from taocheM import locator_m
from taocheM.config_m import config

url = config.home_url


class Logo(Base):

    def test_logo(self):
        """测试首页logo是否展示,@author:xulanzhong"""
        self.driver.get(url)
        logo_is_dispayed = self.driver.is_display(locator_m.Locator_Home.LOGO)

        self.driver.pause(3)

        tt_check.assertTrue(logo_is_dispayed, "首页Logo是否显示：%s" % logo_is_dispayed)


