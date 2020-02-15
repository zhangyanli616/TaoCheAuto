import requests
import unittest
import json
from xmdCW.chewudata.get_data import cheWu
from xmdCW.gettoken.getToken import GetToken
from BeautifulReport import BeautifulReport as bf


class TestXianXiaQianYue(unittest.TestCase, GetToken):

    # @unittest.skip(1)
    def test1_qianyue_status(self):
        """线下签约接口，登录后判断工单是否为待签约状态"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0]
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/query?pageIndex=1&" \
                    "pageSize=10&serviceStatus=102&serviceId=" + danhao
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }

        response_data = requests.get(login_url, headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["data"]["rowCount"], 1)

    # @unittest.skip(1)
    def test2_notoken(self):
        """未登录直接请求线下签约接口"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/contract/paperSign"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            # 'Authorization': GetToken().token()
        }
        request_data = {"serviceId": danhao,
                        "images": [{"latitude": 39.943238,
                                    "longitude": 116.333319,
                                    "cdn": "https://optimize-qa.kanche.com/ydg/vehicle/operation/9761847da2511a720d725e8fdb12bac7.jpg",
                                    "source": "https://images-qa.kanche.com/ydg/vehicle/operation/9761847da2511a720d725e8fdb12bac7.jpg"}]}

        response_data = requests.post(login_url,  json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "用户未登录")

    # @unittest.skip(1)
    def test3_weishouqi(self):
        """未收齐首付款时，选择线下签约"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/contract/paperSign"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }
        request_data = {"serviceId": danhao,
                        "images": [{"latitude": 39.943238,
                                    "longitude": 116.333319,
                                    "cdn": "https://optimize-qa.kanche.com/ydg/vehicle/operation/9761847da2511a720d725e8fdb12bac7.jpg",
                                    "source": "https://images-qa.kanche.com/ydg/vehicle/operation/9761847da2511a720d725e8fdb12bac7.jpg"}]}

        response_data = requests.post(login_url,  json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "云店销售尚未收齐客户首付款。请及时联系总部运营。")

    # @unittest.skip(1)
    def test4_qianyue(self):
        """收齐首付款时，选择线下签约"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/contract/paperSign"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }
        request_data = {"serviceId": danhao,
                        "images": [{"latitude": 39.943238,
                                    "longitude": 116.333319,
                                    "cdn": "https://optimize-qa.kanche.com/ydg/vehicle/operation/9761847da2511a720d725e8fdb12bac7.jpg",
                                    "source": "https://images-qa.kanche.com/ydg/vehicle/operation/9761847da2511a720d725e8fdb12bac7.jpg"}]}

        response_data = requests.post(login_url,  json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "SUCCESS")


if __name__ == "__main__":
    # 定义一个测试集合
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestXianXiaQianYue))
    # 实例化BeautifulReport模块
    run = bf(suite)
    run.report(filename='test', description='登录测试结果')
    # unittest.main()