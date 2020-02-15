# -*- coding:utf-8 -*-
import unittest
from service import AutoTest
from taochePC.config import config

# 企业微信通知名单
from taochePC.test_buycar.test_car_list import CarList
from taochePC.test_buycar.test_detail import Detail
from taochePC.test_homepage.test_carSearchBox import CarSearchResult

to_user = config.to_user

# # 当前目录
# test_dir = "./"
# # 自动加载test_dir下所有以test开头的文件中以test开头的测试方法
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
#
#
# # 生成报告
# runner = ResultHandle(suite=discover, name='淘车PC测试', to_user=to_user, case_type='PC')
# runner.run()


# 调试单个用例
from taochePC.test_homepage.test_buycar import BuyCar
suite = unittest.TestSuite()
suite.addTest(CarSearchResult('test_home_search'))

runner = AutoTest(suite=suite, name='用例调试', to_user=to_user, case_type='PC')
runner.run()
