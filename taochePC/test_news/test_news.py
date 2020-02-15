# -*- coding:utf-8 -*-
from taochePC.config import config
from taochePC import Base
from taochePC import NewsLocator
from titan import tt_check

url = config.news_url


class News(Base):
    def test_nav_selected(self):
        """测试访问资讯站点时导航中资讯是否高亮"""
        # 打开资讯站点
        self.driver.get(url)
        status_actual = self.driver.find_element(NewsLocator.NAV_NEWS).get_attribute('class')

        tt_check.assertEqual(status_actual, 'current', "导航中资讯是否高亮显示")



