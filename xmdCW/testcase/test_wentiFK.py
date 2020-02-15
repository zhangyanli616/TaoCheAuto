import requests
import unittest
import json
from xmdCW.chewudata.get_data import cheWu
from xmdCW.gettoken.getToken import GetToken
from BeautifulReport import BeautifulReport as bf

# 该接口写的是待核准状态的问题反馈，其他状态均类似，都是一个接口


class TestFanKui(unittest.TestCase, GetToken):

    # @unittest.skip(1)
    def test1_fankui_notoken(self):
        """问题反馈接口，未登录直接请求"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/issue-feedback"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            # 未添加token
        }

        response_data = requests.patch(login_url, headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "用户未登录")

    # @unittest.skip(1)
    def test2_fankui_wrongjson(self):
        """登录后，不输入请求参数"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/issue-feedback"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }

        response_data = requests.patch(login_url, headers=headers).json()
        # print(response_data)
        self.assertIn("请求JSON格式不正确", response_data["message"],)

    # @unittest.skip(1)
    def test3_fankui_noid(self):
        """登录后，缺少车务工单号参数，直接请求接口"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/issue-feedback"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }
        request_data = {
            # "serviceId": danhao,
            "serviceStatus": 101,
            "remark": ""
        }
        response_data = requests.patch(login_url, json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "车务工单id不能为空")

    # @unittest.skip(1)
    def test4_fankui_nostatus(self):
        """登录后，缺少车务工单状态参数，直接请求接口"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/issue-feedback"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }
        request_data = {
            "serviceId": danhao,
            # "serviceStatus": 101,
            "remark": ""
        }
        response_data = requests.patch(login_url, json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "当前工单状态不能为空")

    # @unittest.skip(1)
    def test5_fankui_noremark(self):
        """登录后，缺少问题备注参数，直接请求接口"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/issue-feedback"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }
        request_data = {
            "serviceId": danhao,
            "serviceStatus": 101,
            # "remark": ""
        }
        response_data = requests.patch(login_url, json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "问题反馈备注不能为空")

    # @unittest.skip(1)
    def test6_fankui_noremarkcontent(self):
        """登录后，请求参数中问题备注内容为空"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/issue-feedback"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }
        request_data = {
            "serviceId": danhao,
            "serviceStatus": 101,
            "remark": ""
        }
        response_data = requests.patch(login_url, json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "SUCCESS")

    # @unittest.skip(1)
    def test7_fankui_remarkcontentless200(self):
        """登录后，请求参数中问题备注内容有少于200字的内容"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/issue-feedback"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }
        request_data = {
            "serviceId": danhao,
            "serviceStatus": 101,
            "remark": "测试数据"
        }
        response_data = requests.patch(login_url, json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "SUCCESS")

    # @unittest.skip(1)
    def test8_fankui_remarkcontentmore200(self):
        """登录后，请求参数中问题备注内容有大于200字的内容"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/issue-feedback"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }
        remark = "测试数据测试数据测试数据测试数据测测试试测试数据据测据测测试数据试数" \
                 "测试数据测试数据测试数据测试数据测测试试测试数据据测据测测试数据试数" \
                 "测试数据测试数据测试数据测试数据测测试试测试数据据测据测测试数据试数测" \
                 "试数据测试数据测试数据测试数据测测试试测试数据据测据测测试数据试数测试" \
                 "数据测试数据测试数据测试数据测测试试测试数据据测据测测试数据试数测试数据" \
                 "测试数据测试数据测试数据测测试试测试数据据测据测测试数据试数测试数据测" \
                 "试数据测试数据测试数据测测试试测试数据据测据测测试数据试数测试数据测" \
                 "试数据测试数据测试数据测测试试测试数据据测据测测试数据试数"
        request_data = {
            "serviceId": danhao,
            "serviceStatus": 101,
            "remark": remark
        }
        response_data = requests.patch(login_url, json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "SUCCESS")

    # @unittest.skip(1)
    def test9_wrongstatus(self):
        """请求参数中填写的工单状态与实际状态不一致，请求接口"""
        # 获取文件中的车务工单号
        danhao = cheWu()[0].strip('\n')
        # 登录地址
        login_url = "http://uat-c2b.taoche.com/basegate/work/order/"+danhao+"/issue-feedback"
        # 请求头
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': GetToken().token()
        }
        request_data = {
            "serviceId": danhao,
            "serviceStatus": 102,
            "remark": ""
        }
        response_data = requests.patch(login_url, json.dumps(request_data), headers=headers).json()
        # print(response_data)
        self.assertEqual(response_data["message"], "接收消息订单状态与订单状态不匹配")


if __name__ == "__main__":
    # 定义一个测试集合
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFanKui))
    # 实例化BeautifulReport模块
    run = bf(suite)
    run.report(filename='test', description='登录测试结果')
    # unittest.main()
