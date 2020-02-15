# -*- coding:utf-8 -*-
from titan import tt_check
from taocheM.base_m import Base
from taocheM.config_m import TestConfig
from taocheM.locator_m import CarDetail_Locator
from time import sleep
from titan.tt_log import LOG
from titan import SeleniumDriver


detail_url = TestConfig.cardetail_url


# # 详情页点击『服务保障』检查
class SeviceInfo(Base):

    def test_detail_title(self):
        """测试详情页title显示的是否正确@author:zhangyanli"""
        self.driver.get(detail_url)
        detail_title = self.driver.find_element(CarDetail_Locator.DETAIL_TITLE).text
        tt_check.assertEqual("车源详情", detail_title, "车源详情页的title，期望是车源详情，实际是%s" % detail_title)

    def test_avtitiyinfo(self):
        """测试活动信息显示的是否正确@author:zhangyanli"""
        self.driver.get(detail_url)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")

        #查看优惠券信息
        activity_title = self.driver.find_element(CarDetail_Locator.DETAIL_ACTIVITY).text
        LOG.info(activity_title)
        coupon_title = self.driver.find_element(CarDetail_Locator.DETAIL_COUPON).find_elements_by_class_name('y')[0].find_elements_by_tag_name('span')[1].text
        tt_check.assertIn("元优惠券", coupon_title, "优惠券信息显示正常")

        #查看金融特惠信息
        finance = self.driver.find_element(CarDetail_Locator.DETAIL_FINANCE).text
        LOG.info(finance)
        tt_check.assertIn("分期购车享优惠", finance, "金融特惠显示正常")

        #查看赠送服务信息
        service = self.driver.find_element(CarDetail_Locator.DETAIL_SERVICE).text
        LOG.info(service)
        tt_check.assertIn("保修服务",service,"保修服务信息显示正常")

    def test_qgginfo(self):
        """测试全国购信息显示的是否正确@author:zhangyanli"""
        self.driver.get(detail_url)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")
        zhiyinginfo = self.driver.find_element(CarDetail_Locator.DETAIL_ZHIYINGINFO).text
        LOG.info(zhiyinginfo)
        tt_check.assertIn("免费看车",zhiyinginfo,"直营信息显示正常")

    def test_baozhanginfo(self):
        """测试保障信息显示的是否正确@author:zhangyanli"""
        self.driver.get(detail_url)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")
        lable_list = ["保真服务","30天可退","1年保修","店内直卖","包过户"]
        baozhang = self.driver.find_element(CarDetail_Locator.DETAIL_BAOZHANG).find_elements_by_class_name('bx')
        for i in range(len(baozhang)):
            if baozhang[i].text in lable_list:
                print('保障标签：',baozhang[i].text)
            else:
                continue

    def test_archive(self):
        """测试车辆档案评分显示的是否正确@author:zhangyanli"""
        self.driver.get(detail_url)
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")
        score = self.driver.find_element(CarDetail_Locator.DETAIL_SCORE)
        LOG.info(score.text)
        tt_check.assertTrue(score.is_displayed(),"车辆评分数据正常显示")
















