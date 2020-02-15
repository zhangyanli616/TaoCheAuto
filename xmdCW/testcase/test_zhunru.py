import requests
import unittest
import json
from xmdCW.chewudata.get_data import cheWu
from xmdCW.gettoken.getToken import GetToken
from BeautifulReport import BeautifulReport as bf


class TestZhunRu(unittest.TestCase, GetToken):

    # @unittest.skip(1)
    def test1_zhunru_notoken(self):
        """准入接口，未登录直接请求"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0]
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/approval-success"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            # 未添加token
        }

        response_data = requests.patch(login_url, headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "用户未登录")

    # @unittest.skip(1)
    def test2_zhunru_status(self):
        """准入接口，登录后判断工单是否为待核准状态"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0]
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/query?pageIndex=1&" \
                    "pageSize=10&serviceStatus=101&serviceId=" + danhao
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }

        response_data = requests.get(login_url, headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["data"]["rowCount"], 1)

    # @unittest.skip(1)
    def test3_zhunru(self):
        """执行准入操作"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0]
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/approval-success"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }

        response_data = requests.patch(login_url, headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "SUCCESS")


if __name__ == "__main__":
    # 定义一个测试集合
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestZhunRu))
    # 实例化BeautifulReport模块
    run = bf(suite)
    run.report(filename='test', description='登录测试结果')
    # unittest.main()