#登录case
# -*- coding:utf-8 -*-
import unittest
from service import AutoTest
from taocheAPI.config import config
import requests
from titan import tt_check
from titan.tt_log import LOG
from taocheAPI.base import Base
from taocheAPI.test_m_api.common_fuction import M_Login

class TestLoginCase(Base):
    def test_Login_wrongName(self):
        """测试登录接口,异常登录（错误的用户名，正确的密码）,@author:xulanzhong"""
        result = M_Login('1213cf0f055ab878696aef1e75690435', '52b8f71a3056609b657822b2ec3ec70b')
        self.assertEqual(result['Message'], "账号或者密码错误")




