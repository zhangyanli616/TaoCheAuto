# -*- coding:utf-8 -*-

from taocheApp import Base, HomeLoctor,BuyCarLocator
from titan import tt_check

"""首页足迹，品牌推荐，价格区间推荐，级别推荐，全部车源跳转用例检查@author:anyingying"""

class PinPai(Base):
    def test_pinpai(self):
        self.driver.sleep(4)
        # brandNameList = self.driver.find_element(HomeLoctor.PINPAI_ALL_ID).find_elements_by_id('com.ucar.app:id/home_page_brand_text')
        brandNameList = self.driver.find_elements(HomeLoctor.PINPAI_TEXT_IDS)
        if brandNameList:
            for i in range(0,7):
                # 校验前面7个品牌跳转
                brandName = brandNameList[i].text
                # print(brandName)
                brandNameList[i].click()
                self.driver.sleep(2)
                shaixuanText = self.driver.find_element(HomeLoctor.CAR_LIST_SCREEN_ID).find_element_by_class_name('android.widget.TextView').text
                # print("列表页回显关键词为%s" % shaixuanText)
                tt_check.assertEqual(brandName,shaixuanText,"首页品牌推荐区点击的是%s,列表页命中的是%s" % (brandName,shaixuanText))
                self.driver.find_element(HomeLoctor.SHOUYE_ID).click()
                self.driver.sleep(2)
            # 校验品牌楼层“更多”跳转
            brandName = brandNameList[7].text
            print("首页品牌区点击的关键词为%s" % brandName)
            brandNameList[7].click()
            pinpaiTitleText = self.driver.find_element(HomeLoctor.PINPAI_TITLE_ID).text
            print(pinpaiTitleText)
            tt_check.assertEqual("选择品牌",pinpaiTitleText,"首页品牌区域点击“全部”跳转，期望是选择品牌，实际是%s" % pinpaiTitleText)
            pinpaiBack = self.driver.find_element(HomeLoctor.PINPAI_BACK_ID)
            pinpaiBack.click()
            print("回到首页啦！！！")
        else:
            print ("首页没有取到品牌数据")

class JiaGe(Base):
    def test_jiage_name(self):
        self.driver.sleep(4)
        price_expect = ['5万以下', '5-10万', '10-15万', '15万以上','SUV','紧凑型车','小型车','中型车']
        price_actual = []
        priceList = self.driver.find_elements(HomeLoctor.JIAGE_ID)

        for price in priceList:
            price_actual.append(price.text)

        tt_check.assertEqual(price_expect,price_actual,"首页价格&级别楼层，期望是%s,实际是%s" % (price_expect, price_actual))

    def test_jiage_click(self):
        self.driver.sleep(4)
        priceList = self.driver.find_elements(HomeLoctor.JIAGE_ID)
        for i in range(0, 4):
            # 校验推荐价格跳转
            price = priceList[i].text
            priceList[i].click()
            self.driver.sleep(2)
            shaixuanText = self.driver.find_element(HomeLoctor.CAR_LIST_SCREEN_ID).find_element_by_class_name('android.widget.TextView').text
            print("列表页回显关键词为%s" % shaixuanText)
            tt_check.assertEqual(price, shaixuanText, "首页品牌推荐区点击的是%s,列表页命中的是%s" % (price, shaixuanText))
            self.driver.find_element(HomeLoctor.SHOUYE_ID).click()
            self.driver.sleep(2)

    def test_jibie_click(self):
        self.driver.sleep(4)
        jibieList = self.driver.find_elements(HomeLoctor.JIAGE_ID)
        for i in range(4, 8):
            # 校验推荐价格跳转
            jibie = jibieList[i].text
            print(jibie)
            jibieList[i].click()
            self.driver.sleep(2)
            shaixuanText = self.driver.find_element(HomeLoctor.CAR_LIST_SCREEN_ID).find_element_by_class_name('android.widget.TextView').text
            print("列表页回显关键词为%s" % shaixuanText)
            tt_check.assertEqual(jibie, shaixuanText, "首页品牌推荐区点击的是%s,列表页命中的是%s" % (jibie, shaixuanText))
            self.driver.find_element(HomeLoctor.SHOUYE_ID).click()
            self.driver.sleep(2)

class ZuJi(Base):
    def test_zuji(self):
        self.driver.sleep(4)
        zuji_expect = self.driver.find_element(HomeLoctor.ZUJI_PRINT_ID).find_element_by_class_name('android.widget.TextView').text
        print(zuji_expect)
        zuji_actual = "足迹"
        print(zuji_actual)
        if  zuji_expect == zuji_actual :
            print("找到首页足迹楼层啦!")
            jibieList = self.driver.find_elements(HomeLoctor.JIAGE_ID)
            jibie = jibieList[4].text
            jibieList[4].click()
            print ("首页点击级别SUV跳转到列表页了！")
            self.driver.sleep(2)
            self.driver.find_element(HomeLoctor.SHOUYE_ID).click()
            print("回到首页啦!")

            # 取第一个足迹
            zujiList = self.driver.find_elements(HomeLoctor.ZUJI_ITEM_IDS)
            zujiText = zujiList[0].text
            print(zujiText)
            tt_check.assertEqual(jibie, zujiText, "首页点击的是%s,足迹回显的是%s" % (jibie,zujiText))

        else:
            print("首页没有足迹楼层!")

class Home_ALL(Base):
    def test_home_all(self):
        self.driver.sleep(4)
        quanbu = self.driver.find_element(HomeLoctor.HOME_ALL_ID)
        quanbuText = self.driver.find_element(HomeLoctor.HOME_ALL_TEXT_ID).text
        quanbuText_expect = "查看全部车源"
        if quanbuText == quanbuText_expect:
            quanbu.click()
            # 校验页面是否有筛选菜单
            shaixuanMenu = self.driver.find_element(BuyCarLocator.SHAIXUANMENU)
            tt_check.assertTrue(shaixuanMenu, "首页跳转至列表页，列表页显示筛选菜单")

        else:
            print("首页没有找到查看全部车源按钮")





















