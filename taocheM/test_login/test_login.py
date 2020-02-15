from selenium.common.exceptions import ElementNotVisibleException

from titan import tt_check
from taocheM.base_m import Base
from taocheM.config_m import TestConfig
from taocheM.locator_m import Login_Locator
from time import sleep
from titan.tt_log import LOG

login_url = TestConfig.login_url

class Login(Base):

    def test_login_title(self):
        """测试登录页面的Title显示的是否正确@author:zhangyanli"""
        self.driver.get(login_url)
        login_title = self.driver.find_element(Login_Locator.LOGIN_TITLE).text
        tt_check.assertEqual("手机快捷登录", login_title, "登录页面的title，期望是手机快捷登录，实际是%s" % login_title)

    def login(self):
        """手机号密码登录M站"""
        self.driver.get( login_url )
        self.driver.find_element(Login_Locator.LOGIN_PASSWORD_LOGIN).click()
        sleep(2)
        self.driver.find_element(Login_Locator.LOGIN_MOBILE).clear()
        self.driver.find_element(Login_Locator.LOGIN_MOBILE).send_keys('15101013237')
        sleep(1)
        self.driver.find_element(Login_Locator.LOGIN_PASSWORD).clear()
        self.driver.find_element(Login_Locator.LOGIN_PASSWORD).send_keys('abcd1234')
        sleep(1)
        self.driver.find_element(Login_Locator.LOGIN_SUBMITE).click()
        sleep(3)
        #关闭冲屏广告
        # if self.driver.find_element(Login_Locator.LOGIN_ADLAYER).is_displayed():
        #         LOG.info("冲屏广告已显示")
        #         self.driver.find_element(Login_Locator.LOGIN_ADLAYER_CLOSE).click()
        #         sleep(2)
        # else:
        #         LOG.info("冲屏广告未显示")

    def test_login_passwordlogin(self):
        """测试手机号密码登录@author:zhangyanli"""
        self.login()
        self.driver.find_element(Login_Locator.LOGIN_USERCENTER).click()
        sleep(2)
        username = self.driver.find_element(Login_Locator.LOGIN_USERNAME).text
        #tt_check.assertEqual("lily",username,"登录成功后的用户名，期望是lily，实际是%s" %username)
        tt_check.assertIn("3237",username,"登录成功后的手机号包含3237，实际是%s" %username )
