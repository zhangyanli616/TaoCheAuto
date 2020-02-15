from taocheApp import Base, UserCenterLocator
from titan import tt_check


class UserCenterPage(Base):
    def test_login(self):
        """app登录，验证登录用户名@author:fangyu"""
        self.driver.find_element(UserCenterLocator.IMGTABMINE).click()
        self.driver.find_element(UserCenterLocator.TVLOGIN).click()
        self.driver.find_element(UserCenterLocator.PASSWORDDD).click()
        self.driver.find_element(UserCenterLocator.PASSWORDTEL).send_keys('18601089500')
        self.driver.find_element(UserCenterLocator.NEWPASSWORD).send_keys('xf920768781')
        self.driver.find_element(UserCenterLocator.LOGINOK).click()
        username = self.driver.find_element(UserCenterLocator.TVLOGIN).text
        print(username)
        tt_check.assertEqual("淘车用户9500",username,"您登录的账号为:{username}".format(username=username))
