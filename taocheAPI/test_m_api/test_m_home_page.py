# -*- coding:utf-8 -*-
import requests
import json

from taocheAPI.config import config
from taocheAPI.base import Base
from titan import tt_check

sugar_bean_url = config.m_sugar_bean_url



class mHomePage(Base):
    def test_sugar_bean(self):
        """M首页糖豆接口@author:fangyu"""
        sugarBeanTitleList = []
        """首页糖豆接口@author:fangyu"""
        response = requests.get(sugar_bean_url+'c-city-consumer/carSearchTag/getSugarBean?cityId=201&terminalId=3')
        status_code = response.status_code
        if status_code == 200:
            suageBeanData = json.loads(response.text).get('data')
            if suageBeanData:
                for data in suageBeanData:
                    print(data)
                    title = data['title']
                    sugarBeanTitleList.append(title)
                sugarBeanTitleListStr = json.dumps(sugarBeanTitleList, ensure_ascii=False)
                tt_check.assertTrue(True,'当前城市:北京,首页展示的糖豆为:{sugarBeanTitleListStr}'.format(sugarBeanTitleListStr=sugarBeanTitleListStr))
            else:
                tt_check.assertFalse(False,'当前城市:北京,首页糖豆接口返回空')
        else:
            print('接口有问题')
            tt_check.assertFalse(False,'当前城市:北京,首页糖豆接口返回状态为:{status_code}'.format(status_code=status_code))

