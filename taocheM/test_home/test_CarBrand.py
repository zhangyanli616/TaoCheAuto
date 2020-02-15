# -*- coding:utf-8 -*-
#@author:xulanzhong

from titan import tt_check
from taocheM.base_m import Base
from taocheM.locator_m import Locator_Home
from taocheM.config_m import config


url = config.home_url

class CarBrand(Base):

    def test_CarBrand(self):
        """测试默认品牌名称,@author:xulanzhong"""

        brand_expect = ['丰田', '大众', '本田', '奥迪', '宝马', '奔驰', '别克', '更多']

        self.driver.get(url)

        self.driver.pause(2)

        CarBrand_li = self.driver.find_element(Locator_Home.CarBrand_list)
        CarBrand_links = CarBrand_li.find_elements_by_tag_name('a')

        brand_actual = []

        for brand_link in CarBrand_links:
            brand_actual.append(brand_link.text)

        tt_check.assertEqual(sorted(brand_actual), sorted(brand_expect), "我要买车，品牌期望是%s，实际是%s" % (brand_expect, brand_actual))

