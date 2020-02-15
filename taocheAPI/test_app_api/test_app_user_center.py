# -*- coding:utf-8 -*-
import requests
import json

from taocheAPI.base import Base


class AppUserCenter(Base):
    def test_app_login(self):
        """app个人中心-我收藏的记录接口@author:fangyu"""
        ###代码待优化----这只是一个model
        url = "https://appapi.taoche.com/get?action=SignInByPwd&v=7.9.2"
        par = {"mobile": "4IHXEgeGYKRxvzdAG/lLjw==", "password": "xf920768781", "v": "7.9.2"}
        r = requests.post(url, data=par, verify=False)
        r2 = json.loads(r.text).get('data').get('AppUK')
        s = requests.session()
        headers = {
            'AppUK': r2
        }
        url1 = "https://proconsumer.taoche.com/c-appapi/GetUcarFavoriteRecords?v=7.9.2&page=1&size=100"
        r1 = s.get(url1, headers=headers, verify=False)
        print(r1.text)
