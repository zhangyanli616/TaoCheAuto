# -*- coding:utf-8 -*-
#@author:xulanzhong
from titan import tt_check
from taocheM.base_m import Base
from taocheM import locator_m
from taocheM.config_m import config

url = config.list_url


class newsale(Base):

    def newsale(self):
        """测试列表页点击今日上线，查看足迹 列表新标签,@author:xulanzhong"""

        self.driver.get(url)

        self.driver.click(locator_m.Locator_BuyCar.newsale)

       #bz_is_dispayed = self.driver.is_display(locator_m.Locator_BuyCar.newsale_foot)

        newsale_is_dispayed = self.driver.is_display(locator_m.Locator_BuyCar.newsale_label)

        tt_check.assertTrue(newsale_is_dispayed, "今日上线标签是否显示：%s" % newsale_is_dispayed)

