from titan import tt_check
from taocheM.base_m import Base
from taocheM.config_m import TestConfig
from taocheM.locator_m import PingGu_Locator
from time import sleep
from titan.tt_log import LOG
from titan import SeleniumDriver

pinggu_url=TestConfig.pinggu_url

class PingGu(Base):

    def test_pinggu_title(self):
        """测试评估区域Title显示的是否正确@author:zhangyanli"""
        self.driver.get(pinggu_url)
        pinggu_title = self.driver.find_element(PingGu_Locator.PINGGU_TITLE).text
        tt_check.assertEqual("估价", pinggu_title, "评估区域的title，期望是估价，实际是%s" % pinggu_title)

    def test_pinggu_submitclue(self):
        """测试提交评估线索是否正确@author:zhangyanli"""
        self.driver.get(pinggu_url)
        sleep(2)

        #选择车款
        self.driver.find_element(PingGu_Locator.PINGGU_CAR).click()
        sleep(2)
        self.driver.find_elements(PingGu_Locator.PINGGU_CAR_BRAND).pop().click()
        #bb = self.driver.find_element(PingGu_Locator.PINGGU_CAR_BRAND).find_element_by_tag_name('a').find_elements_by_tag_name('span')[1].get_attribute('innerHTML')

        sleep(2)
        self.driver.find_elements( PingGu_Locator.PINGGU_CAR_LIST )[0].find_elements_by_tag_name('a')[0].click()
        sleep(2)
        carlist = self.driver.find_element(PingGu_Locator.PINGGU_CAR_MODLE).find_elements_by_class_name('choose-car-list')

        #选择的车款年份
        carchoose = carlist[0].find_elements_by_tag_name('a')[0].text
        LOG.info("【选择的车款】"+carchoose)
        carmodle = carchoose.split(" ")
        car_first = carmodle[0]
        car_year = car_first[0:4]
        LOG.info("【车款年份】 "+car_year)
        carlist[0].find_elements_by_tag_name('a')[0].click()
        sleep(2)

        #选择上牌时间
        self.driver.find_element(PingGu_Locator.PINGGU_LICENSED_DATE).click()
        a1 = self.driver.find_element(PingGu_Locator.PINGGU_YEAR).find_elements_by_class_name('sub')
        j = -1
        for i in a1:
            j = j + 1
            license_year = i.get_attribute('data-name')
            if car_year in license_year:
                LOG.info("【匹配的上牌年份】 "+license_year)
                self.driver.find_element(PingGu_Locator.PINGGU_YEAR).find_elements_by_class_name('sub')[j].click()
                sleep(1)
                self.driver.find_element(PingGu_Locator.PINGGU_MONTH).find_elements_by_class_name('next')[3].click()
                sleep(2)

        #输入行使里程
        self.driver.find_element(PingGu_Locator.PINGGU_MILE).send_keys('2')
        sleep(2)

        #选择所在城市
        self.driver.find_element(PingGu_Locator.PINGGU_CITY).click()
        sleep(1)
        self.driver.find_element(PingGu_Locator.PINGGU_PROVINCE).find_elements_by_class_name('province')[1].click()
        sleep(1)
        self.driver.find_element(PingGu_Locator.PINGGU_CITY_CHOOSE).find_elements_by_class_name('city2')[0].click()
        sleep(2)

        #输入手机号
        self.driver.find_element(PingGu_Locator.PINGGU_MOBILE).send_keys('13300000000')
        sleep(2)

        #选择估价意向
        self.driver.find_element(PingGu_Locator.PINGGU_INTENTION).click()
        sleep(1)
        self.driver.find_element(PingGu_Locator.PINGGU_INTENTION_CHOOSE).find_elements_by_tag_name('p')[1].click()
        sleep(2)

        #提交估价线索
        self.driver.find_element(PingGu_Locator.PINGGU_ESTIMATE_BUTTON).click()
        sleep(10)

        #查看评估结果页显示是否正确
        tt_check.assertTrue(self.driver.find_element(PingGu_Locator.PINGGU_VALUE_RESULT).is_displayed(),"结果页参考估价数据正常显示")
        tt_check.assertTrue(self.driver.find_element(PingGu_Locator.PINGGU_RELEVANT_CAR).is_displayed(),"结果页相关二手车正常显示")
        tt_check.assertTrue(self.driver.find_element(PingGu_Locator.PINGGU_CHART).is_displayed(),"结果页价格走势图正常显示")














