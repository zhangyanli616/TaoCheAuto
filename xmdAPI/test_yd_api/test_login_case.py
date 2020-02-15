#登录case

from xmdAPI.base import Base
from xmdAPI.test_yd_api.common_fuc import helpLogin


class TestLoginCase(Base):

    # 异常登录（错误的用户名，正确的密码）
    def test_Login_wrongName(self):
        result = helpLogin('liuliuliu', "uat.portal")
        self.assertEqual(result['message'], "CRM登陆失败,用户名不存在")

    # 异常登录（正确的用户名，错误的密码）
    def test_Login_wrongPwd(self):
        result = helpLogin('wb4005', "uat")
        self.assertEqual(result['message'], "CRM登陆失败,用户名或密码不正确")

    # 异常登录（空用户名，空密码）
    def test_Login_empty(self):
        result = helpLogin("", "")
        self.assertEqual(result['message'], "CRM登陆失败")

    # 异常登录（空用户名，正确密码）
    def test_Login_emptyUsername(self):
        result = helpLogin("", "uat.portal")
        self.assertEqual(result['message'], "CRM登陆失败")

    # 异常登录（正确用户名，空密码）
    def test_Login_emptyPwd(self):
        result = helpLogin("wb3002", "")
        self.assertEqual(result['message'], "CRM登陆失败")


    # 异常登录（正确用户名，错误密码（带空格））
    def test_Login_blankspaceUsername(self):
        result = helpLogin("wb3002", "uat.portal ")
        self.assertEqual(result['message'], "CRM登陆失败,用户名或密码不正确")

    #登录成功
    def test_login_success(self):
        result = helpLogin("wb3002", "uat.portal")
        self.assertEqual(result['ok'],True)

    #获得token
    def test_get_token(self):
        result = helpLogin("wb3005", "uat.portal")
        print(result)
        print("token--获得")


