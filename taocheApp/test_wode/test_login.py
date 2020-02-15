import time

from taocheApp import Base, WoDeLoator
from titan import tt_check


class Login(Base):
    def test_login(self):
        """用户名密码登录@author:kangjuan"""
        self.driver.find_element(WoDeLoator.TAB).click()#点击我的TAB
        self.driver.find_element(WoDeLoator.DENGLU).click()#点击登录
        self.driver.find_element(WoDeLoator.PWDL).click()#切换到密码登录
        self.driver.find_element(WoDeLoator.UN).send_keys("17346500242")#输入用户名
        self.driver.find_element(WoDeLoator.PW).send_keys("00000000")  # 输入密码
        self.driver.find_element(WoDeLoator.DL).click()  # 点击登录按钮
        self.driver.sleep(3)
        REALUN=self.driver.find_element(WoDeLoator.DENGLU).text#实际显示用户名
        tt_check.assertEqual("易鑫用户", REALUN, "期望是易鑫用户，实际是%s" % REALUN)

    def test_logout(self):
        """退出登录@author:kangjuan"""
        self.driver.find_element(WoDeLoator.TAB).click()  # 点击我的TAB
        self.driver.sleep(3)
        self.driver.swipeUpDown(0.3,0.1)#滑动页面
        self.driver.sleep(3)
        self.driver.find_element(WoDeLoator.SETTING).click()  # 点击设置
        self.driver.find_element(WoDeLoator.LOGOUT).click()  # 点击退出登录
        self.driver.find_element(WoDeLoator.YES).click()  # 点击确认退出
        self.driver.sleep(2)
        print("aaa")
        self.driver.swipeUpDown(0.7, 0.9)  # 滑动页面
        self.driver.sleep(3)
        REALUN2 = self.driver.find_element(WoDeLoator.DENGLU).text  # 实际显示文案
        tt_check.assertEqual("点击登录", REALUN2, "期望显示文案是点击登录，实际显示文案是是%s" % REALUN2)

    def test_mycollect(self):
        """我收藏的@author:kangjuan"""
        self.driver.find_element(WoDeLoator.TAB).click()#点击我的TAB
        self.driver.find_element(WoDeLoator.COLLECT).click()#点击我收藏的
        REALCOLLECTNAME=self.driver.find_element(WoDeLoator.COLLECTNAME).text  # 收藏页标题
        tt_check.assertEqual("收藏",  REALCOLLECTNAME, "期望是收藏，实际是%s" %  REALCOLLECTNAME)


    def test_mycontact(self):
        """我咨询的@author:kangjuan"""
        self.driver.find_element(WoDeLoator.TAB).click()#点击我的TAB
        self.driver.find_element(WoDeLoator.CONTACT).click()#点击我咨询的
        self.driver.sleep(3)
        REALCONTACTNAME=self.driver.find_element(WoDeLoator.CONTACTNAME).text  # 我咨询的页面标题
        tt_check.assertEqual("我咨询的",  REALCONTACTNAME, "期望是我咨询的，实际是%s" %  REALCONTACTNAME)


    def test_mybrowse(self):
        """我看过的@author:kangjuan"""
        self.driver.find_element(WoDeLoator.TAB).click()#点击我的TAB
        self.driver.find_element(WoDeLoator.BROWSE).click()#点击我看过的
        REALBROWSENAME=self.driver.find_element(WoDeLoator.BROWSENAME).text  # 我看过的页面标题
        tt_check.assertEqual("我看过的",  REALBROWSENAME, "期望是我看过的，实际是%s" %  REALBROWSENAME)


    def test_mypk(self):
        """我对比的@author:kangjuan"""
        self.driver.find_element(WoDeLoator.TAB).click()#点击我的TAB
        self.driver.find_element(WoDeLoator.PK).click()#点击我对比的
        REALPKNAME=self.driver.find_element(WoDeLoator.PKNAME).text  # 我对比的页面标题
        tt_check.assertEqual("对比",  REALPKNAME, "期望是对比，实际是%s" %  REALPKNAME)
