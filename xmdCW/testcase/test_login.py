import requests
import json
import unittest
from BeautifulReport import BeautifulReport as bf


class TestLogin(unittest.TestCase):

    def test1_wrong_name(self):
        """测试输入的用户不存在"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        # 请求URL
        request_url = 'http://uatopenapi.crm.yxqiche.com/baseapi/Account/Login'
        # 请求参数
        request_data = {
            "sourceFlag": 2,
            "account": "wangquan1",
            "password": "uat.portal"
        }
        # 执行登录请求
        response_data = requests.post(request_url, json.dumps(request_data), headers=headers).json()
        self.assertEqual(response_data["message"], "用户不存在")

    def test2_wrong_pwd(self):
        """测试输入的密码不正确"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        # 请求URL
        request_url = 'http://uatopenapi.crm.yxqiche.com/baseapi/Account/Login'
        # 请求参数
        request_data = {
            "sourceFlag": 2,
            "account": "wangquan",
            "password": "uat.portal1"
        }
        # 执行登录请求
        response_data = requests.post(request_url, json.dumps(request_data), headers=headers).json()
        self.assertEqual(response_data["message"], "用户名或密码不正确")

    def test3_no_name(self):
        """测试不输入用户名"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        # 请求URL
        request_url = 'http://uatopenapi.crm.yxqiche.com/baseapi/Account/Login'
        # 请求参数
        request_data = {
            "sourceFlag": 2,
            "account": "",
            "password": "uat.portal1"
        }
        # 执行登录请求
        response_data = requests.post(request_url, json.dumps(request_data), headers=headers).json()
        self.assertEqual(response_data["message"], "参数必填")

    # @unittest.skip(1)
    def test4_no_pwd(self):
        """测试不输入密码"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        # 请求URL
        request_url = 'http://uatopenapi.crm.yxqiche.com/baseapi/Account/Login'
        # 请求参数
        request_data = {
            "sourceFlag": 2,
            "account": "wangquan",
            "password": ""
        }
        # 执行登录请求
        response_data = requests.post(request_url, json.dumps(request_data), headers=headers).json()
        self.assertEqual(response_data["message"], "参数必填")

    def test5_right(self):
        """测试正常登录"""
        headers = {
            'Content-Type': 'application/json;charset=UTF-8'
        }
        # 请求URL
        request_url = 'http://uatopenapi.crm.yxqiche.com/baseapi/Account/Login'
        # 请求参数
        request_data = {
            "sourceFlag": 2,
            "account": "wangquan",
            "password": "uat.portal"
        }
        # 执行登录请求
        response_data = requests.post(request_url, json.dumps(request_data), headers=headers).json()
        self.assertEqual(response_data["message"], None)


if __name__ == "__main__":
    # 定义一个测试集合
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestLogin))
    # 实例化BeautifulReport模块
    run = bf(suite)
    run.report(filename='test', description='登录测试结果')
    # unittest.main()
