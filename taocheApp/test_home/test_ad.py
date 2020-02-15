# -*- coding:utf-8 -*-

from taocheApp import Base, HomeLoctor
from titan import tt_check

"""首页广告用例检查@author:anyingying"""

class AD(Base):
    def test_jiaodiantu(self):
        """焦点图广告"""
        self.driver.sleep(4)
        AD = self.driver.find_element(HomeLoctor.JDAD_ID)
        if AD:
            AD.click()
            self.driver.sleep(2)
            h5Title = self.driver.find_element(HomeLoctor.XINCHEH5_TEXT_ID).text
            tt_check.assertIsNotNone(h5Title,"焦点图广告跳转Title标题为 %s" % h5Title)
            self.driver.find_element(HomeLoctor.XINCHEH5_BACK_ID).click()
        else:
            print("首页未找到焦点图广告！")


    def test_ppzu(self):
        """品牌专区"""
        self.driver.sleep(4)
        print("寻找品牌专区楼层")
        self.driver.swipeUpDown(0.6, 0.1)
        print("定位到品牌专区楼层")
        pinpaiText = self.driver.find_element(HomeLoctor.PPAD_ID).find_element_by_class_name('android.widget.TextView').text

        if pinpaiText:
            tt_check.assertEqual(pinpaiText,"品牌专区","首页有品牌专区广告楼层，期待标题为品牌专区 ,实际是 %s" % pinpaiText)

            self.driver.find_element(HomeLoctor.PPAD1_ID).click()
            self.driver.sleep(2)
            h5Title = self.driver.find_element(HomeLoctor.XINCHEH5_TEXT_ID).text
            tt_check.assertIsNotNone(h5Title,"品牌专区广告跳转Title标题为 %s" % h5Title)
            self.driver.find_element(HomeLoctor.XINCHEH5_BACK_ID).click()


            self.driver.find_element(HomeLoctor.PPAD2_ID).click()
            self.driver.sleep(2)
            h5Title = self.driver.find_element(HomeLoctor.XINCHEH5_TEXT_ID).text
            tt_check.assertIsNotNone(h5Title,"品牌专区广告跳转Title标题为 %s" % h5Title)
            self.driver.find_element(HomeLoctor.XINCHEH5_BACK_ID).click()

            self.driver.find_element(HomeLoctor.PPAD3_ID).click()
            self.driver.sleep(2)
            h5Title = self.driver.find_element(HomeLoctor.XINCHEH5_TEXT_ID).text
            tt_check.assertIsNotNone(h5Title,"品牌专区广告跳转Title标题为 %s" % h5Title)
            self.driver.find_element(HomeLoctor.XINCHEH5_BACK_ID).click()
        else :
            print("首页无品牌专区广告楼层")





