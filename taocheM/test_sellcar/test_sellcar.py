from titan import tt_check
from taocheM.base_m import Base
from taocheM.config_m import TestConfig
from taocheM.locator_m import SellCar_Locator
from taocheM.test_login import test_login
from time import sleep
from titan.tt_log import LOG
from titan import tt_selenium
from titan.tt_log import LOG

sellcar_url=TestConfig.sellcar_url


class SellCar(Base):


    def test_sellcar_title(self):
        """测试我要卖车区域Title显示的是否正确@author:zhangyanli"""
        self.driver.get(sellcar_url)
        sellcar_title = self.driver.find_element(SellCar_Locator.SELL_CAR_TITLE).text
        tt_check.assertEqual("卖车", sellcar_title, "我要卖车区域的title，期望是卖车，实际是%s" % sellcar_title)


    def test_sellcar_submitclue(self):
        """测试提交卖车线索是否成功@author:zhangyanli"""
        test_login.Login.login(self)
        sleep(3)
        self.driver.find_element(SellCar_Locator.SELL_CAR_TAB).click()
        sleep(2)
        self.driver.find_element(SellCar_Locator.SELL_CAR_CITY).click()
        sleep(2)
        self.driver.find_element(SellCar_Locator.SELL_CAR_CHOOSE_CITY).click()
        sleep(2)
        #ele = self.driver.find_element(SellCar_Locator.SELL_CAR_BUTTON)
        #self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        #self.driver.execute_script("arguments[0].click();", ele)
        #sleep(1)

        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element(SellCar_Locator.SELL_CAR_BUTTON).click()
        sleep(2)
        LOG.info("【免费看车提交成功】")









