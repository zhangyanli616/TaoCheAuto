import requests
import json


class GetToken:
    @staticmethod
    def token():
        # 请求头
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
        # 返回请求数据
        return response_data["data"]


if __name__ == "__main__":
    result = GetToken().token()
    print(result["data"])