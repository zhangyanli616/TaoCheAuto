from taocheApp import Base, HomeLoctor,CarDetails
from titan import tt_check

class TuiJian(Base):
    def test_tuijian_floor(self):
        """首页推荐区点击检查@author:anyingying"""
        self.driver.sleep(4)
        print("寻找推荐楼层")
        self.driver.swipeUpDown(0.4, 0.1)
        print("定位到推荐楼层")

        mainTitleList = self.driver.find_elements(HomeLoctor.JINRISHANGXIN_TEXT_IDS)
        if mainTitleList:
            mainTitletext = mainTitleList[0].text
            print(mainTitletext)
            tt_check.assertEqual("今日上新",mainTitletext,"推荐区域主标题，期望是今日上新，实际是%s" % mainTitletext)
            # 测试今日上新&越野SUV
            reclist = self.driver.find_elements(HomeLoctor.JINRISHANGXIN_IDS)
            for rec in reclist:
                rec.click()
                self.driver.sleep(2)
                shaixuanText = self.driver.find_element(HomeLoctor.CAR_LIST_SCREEN_ID).find_element_by_class_name('android.widget.TextView').text
                print("列表页回显关键词为%s" % shaixuanText)
                tt_check.assertIn(shaixuanText ,"今日上新或者SUV", "期望是今日上新或者SUV，实际是%s" % shaixuanText)
                self.driver.find_element(HomeLoctor.SHOUYE_ID).click()
                self.driver.sleep(1)

            #测试准新车&超低月供&城市代步
            recslist = self.driver.find_elements(HomeLoctor.ZHUNXINCHE_IDS)
            for recs in recslist:
                recs.click()
                self.driver.sleep(2)
                shaixuanText = self.driver.find_element(HomeLoctor.CAR_LIST_SCREEN_ID).find_element_by_class_name(
                    'android.widget.TextView').text
                print("列表页回显关键词为%s" % shaixuanText)
                tt_check.assertIn(shaixuanText ,"准新车或2000元以下或20万以下", "期望是准新车或2000元以下或20万以下，实际是%s" % shaixuanText)
                self.driver.find_element(HomeLoctor.SHOUYE_ID).click()
                self.driver.sleep(1)

        else:
            print("首页没有取到推荐楼层")


    def test_usedcar_floor(self):
        """首页二手车推荐楼层(车源特色)检查@author:anyingying"""
        self.driver.sleep(4)
        print("寻找二手车推荐楼层")
        self.driver.swipeUpDown(0.55, 0.1)
        usedCarText= self.driver.find_element(HomeLoctor.USEDCARREC_ID).find_element_by_class_name('android.widget.TextView').text
        usedCarText_Expect = "二手车推荐"
        usedCarText_Actual = str(usedCarText)
        if usedCarText_Actual == usedCarText_Expect :
            print("首页有二手车推荐楼层")
            carTeseList = self.driver.find_elements(HomeLoctor.USEDCARTESE_IDS)
            a = len(carTeseList)
            for i in range(0,a):
                carTeseTitle = carTeseList[i].find_element_by_id('com.ucar.app:id/tv_tab_title')
                carTeseTitle_text = carTeseTitle.text
                tt_check.assertIsNotNone(carTeseTitle_text, "二手车推荐楼层车源特色标题为 %s" % carTeseTitle_text)

        else:
            print("首页无二手车推荐楼层")

    def test_usedcar_click(self):
        """首页二手车推荐楼层(车辆点击)检查@author:anyingying"""
        self.driver.sleep(4)
        print("寻找二手车推荐楼层")
        self.driver.swipeUpDown(0.55, 0.1)
        carContent = self.driver.find_element(HomeLoctor.USEDCAR_CONTENT_ID)
        if carContent:
            print("二手车推荐楼层有车源！")
            usedcarList = self.driver.find_elements(HomeLoctor.USEDCARLIST_IDS)
            usedcarPrice_text = self.driver.find_element(HomeLoctor.USEDCARPRICE_ID).text
            usedcarList[0].click()
            print("跳转车源详情页啦！")
            carPriceSales_text = self.driver.find_element(CarDetails.CARPRICE_SALES).text
            tt_check.assertEqual(usedcarPrice_text,carPriceSales_text,"二手车推荐楼层列表页价格为 %s,详情页价格为 %s" % (usedcarPrice_text,carPriceSales_text))

        else:
            print("二手车推荐楼层无车源！")


    def test_usedcar_slide(self):
        """首页二手车推荐楼层(滑动查看全部)检查@author:anyingying"""
        self.driver.sleep(5)
        self.driver.swipeUpDown(0.55,0.2)
        self.driver.sleep(2)
        self.driver.swipe(0.55,0.6,0.1,0.6)
        self.driver.sleep(2)
        # self.driver.swipeLeftRight(0.55,0.1)
        # 这块滑动靠运气 找不到准确一定的坐标，待优化
        print("预期页面露出二手车推荐楼层继续滑动查看全部元素")
        usedCarMore_text = self.driver.find_element(HomeLoctor.USEDCARMORE_ID).text
        tt_check.assertEqual("继续滑动查看全部",usedCarMore_text,"%s显示出来了"%usedCarMore_text)











