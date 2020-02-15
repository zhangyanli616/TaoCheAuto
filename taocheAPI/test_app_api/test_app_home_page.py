# -*- coding:utf-8 -*-
import requests
import json

from taocheAPI.config import config
from taocheAPI.base import Base
from titan import tt_check

sugar_bean_url = config.app_sugar_bean_url



class AppHomePage(Base):
    def test_sugar_bean(self):
        """App首页糖豆接口@author:fangyu"""
        sugarBeanTextList = []
        response = requests.get(sugar_bean_url+'get?action=gethomepagenew&v=7.9.0&cid=201&latitude=39.937341&longitude=116.320197&random=1409')
        status_code = response.status_code
        if status_code == 200:
            pageLabelList = json.loads(response.text).get('data').get('PageLabelList')
            if pageLabelList:
                for label in pageLabelList:
                    print(label)
                    text = label['Text']
                    sugarBeanTextList.append(text)
                sugarBeanTextListStr = json.dumps(sugarBeanTextList, ensure_ascii=False)
                tt_check.assertTrue(True,'当前城市：北京，首页展示的糖豆为:{sugarBeanTextListStr}'.format(sugarBeanTextListStr=sugarBeanTextListStr))
            else:
                tt_check.assertFalse(False,'当前城市：北京，首页糖豆接口返回空')
        else:
            tt_check.assertFalse(False,'当前城市：北京，首页糖豆接口返回状态为:{status_code}'.format(status_code=status_code))

