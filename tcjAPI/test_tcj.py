import unittest
import requests
import json
import random
# import uiautomator


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """淘车检登录接口"""
        url = 'http://test.appapijc.yxqiche.com/user/login'


        headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Connection': 'keep-alive'
                }
        request_param = {
            'deviceInfo':'863454036115397|3.1.4|5.1.1|22|0|vivo|vivo X7',
            'password':'b9kq5RFwZDJqOIJbSAht2w\u003d\u003d',
            'account':'15811055530',
        }
        response = requests.post(url,data = json.dumps(request_param), headers=headers)
        print('登录接口返回值： '  + response.text)
        self.token =  response.json()['data']['token']


    # @unittest.skip
    def test01_djclist(self):

        """待检测列表接口"""
        url = 'http://test.appapijc.yxqiche.com/task/getUnDetectList'

        headers_get = {
             'Content-Type': 'application/json;charset=UTF-8',
             'Connection': 'keep-alive',
             'token':self.token,
        }

        request_param = {
            'pageIndex':1,
            'pageSize':10,
         }
        response_message = requests.get(url,request_param,headers = headers_get)
        print('待检测列表返回值： ' + response_message.text)
        self.assertEqual(response_message.text[1:11], '"code":200', '接口返回错误，状态码非200')

    # @unittest.skip
    def test02_bendigou(self):

        """自建工单-异地购接口"""
        #
        url  = 'http://test.appapijc.yxqiche.com/task/postCreateTaskInfo'
        vin = 'LIUNKI890JKN4' + str(random.randint(1000,9999))

        request_param = {
            "BrandId":2,
            "CarCityId":540400,
            "CarCityName":"林芝市",
            "CarLicenseNo":"京A86666",
            "CarName":"奔驰A级 - 2019款 A 200 L",
            "CarProvinceId":540000,
            "CarTypeId":129308,
            "CarVinCode":vin,
            "SerialId":5381,
            "bizType":4,
            "brandName":"奔驰",
            "carTypeName":"2019款 A 200 L",
            "channelType":0,
            "ignoreCases":[],
            "licenseCityId":540400,
            "licenseCityName":"林芝市",
            "licenseProvinceId":540000,
            "sellDetect":0,
            "serialName":"奔驰A级",
            "storeId":"254880",
            "storeName":"B2C采集异地购",
            "storePhone":"16649499494",
            "storeType":2,
        }

        headers = {
             'Content-Type': 'application/json;charset=UTF-8',
             'Connection': 'keep-alive',
             'token':self.token,
        }

        response_message = requests.post(url,data=json.dumps(request_param),headers = headers)
        self.orderNo = response_message.json()['data']['orderNo']
        print(response_message.text)
        self.assertEqual(response_message.text[1:11], '"code":200', '接口返回错误，状态码非200')
        print('自建工单ID： ' + self.orderNo)


    # @unittest.skip
    def test03_working(self):

        """首页工作台接口"""
        url = 'http://test.appapijc.yxqiche.com/task/getsummary'

        headers = {
             'Content-Type': 'application/json;charset=UTF-8',
             'Connection': 'keep-alive',
             'token':self.token,
        }
        response_message = requests.get(url,headers = headers)
        print('首页工作台返回值： ' + response_message.text)
        self.assertEqual(response_message.text[1:11], '"code":200', '接口返回错误，状态码非200')

    # @unittest.skip
    def test04_message(self):

        """消息接口"""
        url = 'http://test.appapijc.yxqiche.com/recheck/rechecklist'

        headers = {
             'Content-Type': 'application/json;charset=UTF-8',
             'Connection': 'keep-alive',
             'token':self.token,
        }

        request_param = {
            'pageIndex':1,
            'pageSize':10,
         }

        response_message = requests.get(url,request_param,headers = headers)
        print('消息接口返回值： ' + response_message.text)
        self.assertEqual(response_message.text[1:11], '"code":200','接口状态码非200')

    # @unittest.skip
    def test05_OrderDetected(self):
        """检测失败接口"""

        url = 'http://test.appapijc.yxqiche.com/report/postOrderDetectedInfo'

        headers = {
             'Content-Type': 'application/json;charset=UTF-8',
             'Connection': 'keep-alive',
             'token':self.token,
        }

        request_param = {
            "taskNo":"156860261702814",
            "orderNo":'Y20570460',
            "reason":"c1_clys",
            "remark":""
        }

        response_message = requests.post(url,data= json.dumps(request_param),headers = headers)

        if response_message.text[1:11] == '"code":200' :
            self.assertEqual(response_message.text[1:11], '"code":200', '接口状态码非200')
            print('检测失败接口: ' + response_message.text)
        elif response_message.text[1:11] == '"code":500' :
            self.assertEqual(response_message.text[1:11], '"code":500', '接口状态码非200')
            print('检测失败接口: ' + response_message.text)
        else:
            self.assertEqual(True,False,'接口返回错误')

    # @unittest.skip
    def test06_vinCode(self):

        """vin码排重查询接口"""

        url = 'http://test.appapijc.yxqiche.com/inspectionreport/validateVIN'

        headers = {
             'Content-Type': 'application/json;charset=UTF-8',
             'Connection': 'keep-alive',
             'token':self.token,
        }

        request_param = {
            'vinCode': 'LXVD3GFC2GA031284',
            'vehicleId': '',
            'bizType': 'ydg',
        }

        response_message = requests.get(url,request_param,headers = headers)
        if response_message.text[1:11] == '"code":200' :
            self.assertEqual(response_message.text[1:11], '"code":200', '接口状态码非200')
            print('vin码排重查询接口: ' + response_message.text)
        elif response_message.text[1:11] == '"code":500' :
            self.assertEqual(response_message.text[1:11], '"code":500', '接口状态码非200')
            print('vin码排重查询接口: ' + response_message.text)
        else:
            self.assertEqual(True,False,'接口返回错误')

    # @unittest.skip
    def test07_weibao(self):

        """维保查询接口"""

        url = 'http://test.appapijc.yxqiche.com/inspectionreport/getKeepRecord'

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Connection': 'keep-alive',
            'token': self.token,
        }
        request_param = {
            "orderType":0,
            "orderId":"",
            "format":"url",
            "vin":"LXVD3GFC2GA031284",
            "from":""
        }

        response_message = requests.post(url,json.dumps(request_param),headers = headers)
        if response_message.text[1:11] == '"code":200' :
            self.assertEqual(response_message.text[1:11], '"code":200', '接口状态码非200')
            print('维保查询接口: ' + response_message.text)
        elif response_message.text[1:11] == '"code":500' :
            self.assertEqual(response_message.text[1:11], '"code":500', '接口状态码非200')
            print('维保查询接口: ' + response_message.text)
        else:
            self.assertEqual(True,False,'接口返回错误')

    # @unittest.skip
    def test08_shop(self):

        """获取店铺接口"""

        url = 'http://test.appapijc.yxqiche.com/ydg/getStore'

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Connection': 'keep-alive',
            'token': self.token,
        }

        request_param = {
            "searchType":2,
            "searchKeywords":"",
            "pageIndex":1,
            "pageSize":20,
        }

        response_message = requests.get(url, request_param, headers=headers)
        print('获取店铺接口： ' + response_message.text)
        self.assertEqual(response_message.text[1:11], '"code":200', '接口状态码非200')

    # @unittest.skip
    def test09_daishangjia(self):

        """待上架列表接口"""

        url = 'http://test.appapijc.yxqiche.com/carsource/getShelveCarList'

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Connection': 'keep-alive',
            'token': self.token,
        }

        request_param = {
            "pageIndex":1,
            "pageSize":10,
            "shelveStatus":0,
        }

        response_message = requests.get(url, request_param, headers=headers)
        print('待上架列表接口： ' + response_message.text)
        self.assertEqual(response_message.text[1:11], '"code":200', '接口状态码非200')

    # @unittest.skip
    def test10_TaskList(self):

        """上传完成列表接口"""

        url = 'http://test.appapijc.yxqiche.com/task/getHistoryTaskList'

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Connection': 'keep-alive',
            'token': self.token,
        }

        request_param = {
            "pageIndex":1,
            "pageSize":10,
            "queryType":1,
            "sortType":4
        }
        response_message = requests.get(url, request_param, headers=headers)
        print('上传完成列表接口： ' + response_message.text)
        self.assertEqual(response_message.text[1:11], '"code":200', '接口状态码非200')

    # @unittest.skip
    def test11_falList(self):

        """上架失败列表接口"""

        url = 'http://test.appapijc.yxqiche.com/carsource/getShelveCarList'

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'Connection': 'keep-alive',
            'token': self.token,
        }

        request_param = {
            "pageIndex":1,
            "pageSize":10,
            "shelveStatus":3,
        }

        response_message = requests.get(url, request_param, headers=headers)
        print('上架失败列表接口： ' + response_message.text)
        self.assertEqual(response_message.text[1:11],'"code":200','接口返回错误，状态码非200')

    # @unittest.skip
    def test12_shangjia(self):
        """上架车辆接口"""
        url = 'http://test.appapijc.yxqiche.com/inspectionreport/submitSaleInfo'

        headers = {
             'Content-Type': 'application/json;charset=UTF-8',
             'Connection': 'keep-alive',
             'token':self.token,
        }

        request_param = {
            "buyPrice": "10000",
            "midPrice": "0",
            "saleLabelType": "",
            "saleRemark": "",
            "saleType": "",
            "unifiedNumber": "000552653"
        }

        response_message = requests.post(url,data= json.dumps(request_param), headers=headers)
        print('操作上架接口： ' + response_message.text)

if __name__ == '__main__':
    unittest.main()



