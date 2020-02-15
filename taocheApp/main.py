# -*- coding:utf-8 -*-
import unittest
from service import AutoTest
from taocheApp.config import config

# 企业微信通知名单
from taocheApp.test_buycar.test_buycar import BuyCar
from taocheApp.test_home.test_page_click import HomePage

from taocheApp.test_home.test_tangdou import TangDou

to_user = config.to_user

# # 当前目录
# test_dir = "./"
# # 自动加载test_dir下所有以test开头的文件中以test开头的测试方法
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
#
#
# # 生成报告
# runner = ResultHandle(suite=discover, name='淘车App测试', to_user=to_user, case_type='APP')
# runner.run()


# 调试单个用例
suite = unittest.TestSuite()
#suite.addTest(TuiJian('test_tuijian_floor'))
#suite.addTest(SellCar('test_sellcar'))
#suite.addTest(BuyCar('test_buycarjiage'))
#suite.addTest(BuyCar('test_buycarsearch'))
suite.addTest(HomePage('test_vendon_floor_show'))
#suite.addTest(Login('test_login'))

runner = AutoTest(suite=suite, name='App用例调试', to_user=to_user, case_type='APP')
runner.run()
