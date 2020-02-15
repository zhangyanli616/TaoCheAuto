# -*- coding:utf-8 -*-
#@author:xulanzhong
from titan import tt_check
from taocheM.base_m import Base
from taocheM import locator_m
from taocheM.config_m import config

url = config.list_url


class SearchQgg(Base):

    def SearchQgg(self):
        """测试列表页点击全国购，查看足迹 列表新标签,@author:xulanzhong"""

        self.driver.get(url)

        self.driver.click(locator_m.Locator_BuyCar.SearchQgg)

       #bz_is_dispayed = self.driver.is_display(locator_m.Locator_BuyCar.newsale_foot)

        Qgg_is_dispayed = self.driver.is_display(locator_m.Locator_BuyCar.SearchQgg_label)

        tt_check.assertTrue(Qgg_is_dispayed, "全国购标签是否显示：%s" % Qgg_is_dispayed)

