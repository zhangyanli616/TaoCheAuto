import time

from taocheApp import Base, BuyCarLocator,SellCarLocator
from titan import tt_check




class SellCar(Base):
    def test_sellcar(self):
        """app卖车tab跳转@author:kangjuan"""
        self.driver.find_element(SellCarLocator.TAB).click()
        titleText=self.driver.find_element(SellCarLocator.TITLE).text
        tt_check.assertIn("卖车",titleText, "期望是卖车，实际是%s" % titleText)








