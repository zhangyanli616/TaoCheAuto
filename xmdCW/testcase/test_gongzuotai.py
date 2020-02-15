import requests
import unittest
from xmdCW.gettoken.getToken import GetToken
from BeautifulReport import BeautifulReport as bf


class TestGongDan(unittest.TestCase, GetToken):

    def test1_gongzt(self):
        """工作台，工单统计接口，正常登录后请求"""
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/statistics"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }

        response_data = requests.get(login_url, headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "SUCCESS")

    # @unittest.skip(1)
    def test2_gongzt_notoken(self):
        """工作台，工单统计接口，不登录直接请求"""
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/statistics"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            # 没有添加token
        }

        response_data = requests.get(login_url, headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "用户未登录")


if __name__ == "__main__":
    # 定义一个测试集合
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGongDan))
    # 实例化BeautifulReport模块
    run = bf(suite)
    run.report(filename='test', description='登录测试结果')
    # unittest.main()