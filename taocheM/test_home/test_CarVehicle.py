# -*- coding:utf-8 -*-
#@author:xulanzhong

from titan import tt_check
from taocheM.base_m import Base
from taocheM.locator_m import Locator_Home
from taocheM.config_m import config


url = config.home_url

class CarVehicle(Base):

    def test_CarVehicle(self):
        """测试默认车型糖豆,@author:xulanzhong"""

        CarVehicle_expect = ['SUV', '紧凑型车', '小型车', '中型车']

        self.driver.get(url)

        CarVehicle_li = self.driver.find_element(Locator_Home.CarVehicle_list)
        CarVehicle_links = CarVehicle_li.find_elements_by_tag_name('a')

        Vehicle_actual = []

        for Vehicle_link in CarVehicle_links:
            Vehicle_actual.append(Vehicle_link.text)

        tt_check.assertEqual(sorted(Vehicle_actual), sorted(CarVehicle_expect), "我要买车，品牌期望是%s，实际是%s" % (CarVehicle_expect, Vehicle_actual))

