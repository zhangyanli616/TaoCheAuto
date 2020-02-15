import time

from taocheApp import Base, BuyCarLocator,SellCarLocator
from titan import tt_check
from titan.tt_check import assertGreaterEqual


class BuyCar(Base):
    def test_buycarjiage(self):
        """app买车tab筛选100万以上车源满价格最低排序@author:kangjuan"""
        self.driver.find_element(BuyCarLocator.TAB).click()#点击买车TAB
       #self.driver.find_element(BuyCarLocator.CITY).click()#打开城市选择框
       #self.driver.find_element(BuyCarLocator.SY).click()#选择沈阳
       # self.driver.find_element(BuyCarLocator.CITY_CLOSE).click()#关闭城市选择框
        self.driver.find_element(BuyCarLocator.JG).click()#点击价格筛选框
        self.driver.find_element(BuyCarLocator.JG1).click()#选择价格100万以上
        self.driver.find_element(BuyCarLocator.PX).click()#点击排序筛选框
        self.driver.find_element(BuyCarLocator.JGZD).click()#选择价格最低
        Text=self.driver.find_element(BuyCarLocator.JGFIRST).text #第一辆车的价格
        Text1= Text.split('万')
        Text2=Text1[0]
        Text3=float(Text2)
        assertGreaterEqual(Text3, 100,"筛选100万以上车源中价格最低的车源价格为%s" % Text3 )
       # print("筛选的100万以上的车源中价格最低的车源价格是",Text)


    def test_buycarsearch(self):
         """app买车tab搜索奥迪@author:kangjuan"""
         self.driver.find_element(BuyCarLocator.TAB).click()  # 点击买车TAB
         self.driver.find_element(BuyCarLocator.SEARCH).click()# 点击搜索框
         self.driver.find_element(BuyCarLocator.SEARCH_INPUT).click()  #搜索页点击搜索框
         self.driver.send_keys("奥迪")
         Ppname=self.driver.find_element(BuyCarLocator.PPHX).text
         tt_check.assertEqual("奥迪", Ppname, "期望是奥迪，实际是%s" % Ppname)



















