from taocheApp import Base, HomeLoctor
from titan import tt_check

class XinChe(Base):
    def test_xinche_floor(self):
        """首页新车楼层点击检查@author:anyingying"""
        self.driver.sleep(4)
        print("寻找新车楼层")
        self.driver.swipeUpDown(0.55, 0.1)
        # 点击新车推荐
        self.driver.find_element(HomeLoctor.XINCHETUIJIAN_ID).click()
        print("进入新车推荐H5页面")
        self.driver.sleep(2)
        XinCheText = self.driver.find_element(HomeLoctor.XINCHEH5_TEXT_ID).text
        tt_check.assertIn("淘车新车", XinCheText, "期望是淘车新车，实际是%s" % XinCheText)
        self.driver.find_element(HomeLoctor.XINCHEH5_BACK_ID).click()
        self.driver.sleep(1)

        # 点击开走吧
        self.driver.find_element(HomeLoctor.KAIZOUBA_ID).click()
        print("进入开走吧H5页面")
        self.driver.sleep(2)
        XinCheText = self.driver.find_element(HomeLoctor.XINCHEH5_TEXT_ID).text
        tt_check.assertIn("开走吧", XinCheText, "期望是开走吧，实际是%s" % XinCheText)
        self.driver.find_element(HomeLoctor.XINCHEH5_BACK_ID).click()
        self.driver.sleep(1)

        # 点击分期购车
        self.driver.find_element(HomeLoctor.FENQIGOUCHE_ID).click()
        print("进入分期购车H5页面")
        self.driver.sleep(2)
        XinCheText = self.driver.find_element(HomeLoctor.XINCHEH5_TEXT_ID).text
        tt_check.assertIn("分期购车", XinCheText, "期望是淘车分期，实际是%s" % XinCheText)
        self.driver.find_element(HomeLoctor.XINCHEH5_BACK_ID).click()
        self.driver.sleep(1)
