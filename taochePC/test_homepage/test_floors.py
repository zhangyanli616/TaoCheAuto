# -*- coding:utf-8 -*-
from titan import tt_check
from taochePC import Base
from taochePC.config import config
from taochePC import HomePageLocator

home_url = config.home_url


class Floors(Base):
    def test_floor(self):
        """测试首页楼层显示是否正确"""
        floors_expected = ["全国购", "淘车推荐", "品牌认证车", "淘车新车", "资讯"]
        floors_actual = []
        self.driver.get(home_url)
        floors_spans = self.driver.find_elements(HomePageLocator.FLOORS)

        for floor in floors_spans:
            # 排除不确定的楼层
            if floor.text != '商家急售车':
                floors_actual.append(floor.text)

        tt_check.assertEqual(floors_actual, floors_expected,
                             "首页楼层期望是%s，实际是%s" % (floors_expected, floors_actual))

