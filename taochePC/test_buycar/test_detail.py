# -*- coding:utf-8 -*-
import time

import requests

from taochePC.config import config

from taochePC import Base, BuyCarLocator,HomePageLocator
from titan import tt_check


buy_car_url = config.bugcar_url
buycar_collect_url =config.buycar_collect_url


class Detail(Base):

    def test_car_info(self):
        """验证详情页车源基本信息与选中的车源是否一致@author:fangyu"""
        self.driver.get(buy_car_url)
        self.driver.find_element(BuyCarLocator.CAR_LIST_INFO).click()
        self.driver.switch_to_window()
        brand_name = self.driver.find_element(BuyCarLocator.CAR_DETAIL_INFO).text
        print('进入车源：{brand_name} 的详情页'.format(brand_name=brand_name))
        city_name = self.driver.find_element(BuyCarLocator.CITY_INFO).text
        time.sleep(2)
        if city_name == '郑州' or city_name == '沈阳' or city_name == '东莞':
            dealer_url = self.driver.find_element(BuyCarLocator.DEALER_INFO).get_attribute('href')
            print("当前城市:{city_name},对应的店铺地址:{dealer_url}".format(city_name=city_name,dealer_url=dealer_url))
            r = requests.get(dealer_url)
            status = r.status_code

            if status != 200:
                tt_check.assertFalse(False, '当前城市为:{city_name}，当前店铺地址为:{dealer_url},该店铺的请求状态为:{status}'.
                                     format(city_name=city_name, dealer_url=dealer_url, status=status))
            else:
                tt_check.assertFalse(False, '当前城市为:{city_name}，当前店铺地址为:{dealer_url},该店铺的请求状态为:{status}'.
                                     format(city_name=city_name, dealer_url=dealer_url, status=status))

        else:
            print('ignore')

    def test_addCollect(self):
        """验证详情页车源的收藏功能@author:gaoxinling"""
        self.driver.get(buycar_collect_url)
        #点击加入收藏
        self.driver.find_element(HomePageLocator.BUY_CAR_COLLECT).click()
        time.sleep(2)
        #点击右侧车源收藏侧边栏
        addCollect = self.driver.find_element(HomePageLocator.BUY_CAR_COLLECTED).click()
        time.sleep(2)
        #获取收藏的车源名称
        Vehicle_addCollect= self.driver.find_element(HomePageLocator.BUY_CAR_COLLECTED_text).text
        print('您收藏的车源是:'+ Vehicle_addCollect)
        #获取该车源的实际名称
        Vehicle_name =self.driver.find_element(HomePageLocator.Vehicle_name).text
        print('您收藏的车源是:' + Vehicle_name)
        #self.assertAlmostEqual(self,Vehicle_addCollect,Vehicle_name)
        ss = Vehicle_name.split("-", 4)
        re = tt_check.assertIn(ss[1],Vehicle_name,"检测收藏的车源名称与实际的车源名称相符")












