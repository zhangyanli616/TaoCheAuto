# -*- coding:utf-8 -*-

from taocheApp import Base, HomeLoctor
from titan import tt_check

class TangDou(Base):
    def test_tangdou_name(self):
        """首页糖豆名称检查@author:anyingying"""
        # 以北京地区糖豆为测试点
        self.driver.sleep(4)
        #取糖豆
        sugerList = self.driver.find_element(HomeLoctor.TANGDOU_ALL_IDS).find_elements_by_id('com.ucar.app:id/sugar_peas_root')

        for i in range(0,10):
            sugerNameText = sugerList[i].find_element_by_id('com.ucar.app:id/sugar_peas_name').text
            # print(sugerNameText)
            sugerNameExpect = ['买二手车','全国购','分期购','保真车','金融特惠','帮我找车','估价','练手车','明星车','新车']
            # print(sugerNameExpect[i])
            tt_check.assertEqual(sugerNameExpect[i],sugerNameText,"北京地区第%s个糖豆期望是%s,实际是%s" %(i+1,sugerNameExpect[i],sugerNameText))
