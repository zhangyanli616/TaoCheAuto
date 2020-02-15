# -*- coding:utf-8 -*-
import sys
print(sys.path)
sys.path.append("C:\\Users\\zhangyanli\\AppData\\Local\\Programs\\Python\\Python37\\python.exe")
sys.path.append("D:/Program Files (x86)/Jenkins/workspace/TestTaoche/taocheM/main_M.py")
sys.path.append("D:\\Program Files (x86)\\Jenkins\\workspace\\TestTaoche\\taocheM")
sys.path.append("D:\\Program Files (x86)\\Jenkins\\workspace\\TestTaoche")
sys.path.append("C:\\Users\\zhangyanli\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip")
sys.path.append("C:\\Users\\zhangyanli\\AppData\\Local\\Programs\\Python\\Python37\\DLLs")
sys.path.append("C:\\Users\\zhangyanli\\AppData\\Local\\Programs\\Python\\Python37\\lib")
sys.path.append("C:\\Users\\zhangyanli\\AppData\\Local\\Programs\\Python\\Python37")
sys.path.append("C:\\Users\\zhangyanli\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages")
sys.path.append("C:\\Users\\zhangyanli\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\pip-19.0.3-py3.7.egg")
sys.path.append("E:\\Program Files\\JetBrains\\PyCharm 2018.3.1\\helpers\\pycharm_matplotlib_backend")


import unittest

from service import AutoTest
from taocheM.config_m import config

#from taocheM.test_home.test_Hotsearch import Hotsearch
from taocheM.test_detail.test_service_assurance import Service

to_user = config.to_user


from taocheM.test_buycar.test_SearchNewsale import newsale
from taocheM.test_buycar.test_Searchprice import searchprice
from taocheM.test_buycar.test_SearchQGG import SearchQgg
from taocheM.test_home.test_CarBrand import CarBrand
from taocheM.test_home.test_CarPrice import CarPrice
from taocheM.test_home.test_CarShop import CarShop
from taocheM.test_home.test_CarVehicle import CarVehicle
from taocheM.test_home.test_Hotsearch import Hotsearch
from taocheM.test_home.test_Logo import Logo
from taocheM.test_home.test_Recommend import Recommend
from taocheM.test_home.test_sugarbean import SugarBean
from taocheM.test_home.test_CarBrand import CarBrand
from taocheM.test_home.test_Newcar import Newcar
from taocheM.test_sellcar.test_sellcar import SellCar
from taocheM.test_pinggu.test_pinggu import PingGu
from taocheM.test_login.test_login import Login
from taocheM.test_detail.test_bzcintro import SeviceInfo
from taocheM.test_detail.test_carconfig import Config
from taocheM.test_detail.test_carreport import Report





#执行所有测试用例
# test_dir = "./"
# # 自动加载test_dir下所有以test开头的文件中以test开头的测试方法
# discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
# runner = AutoTest(suite=discover, name='用例调试',to_user=to_user, case_type='PC', env=env)
# runner.run()




# 调试单个用例


suite = unittest.TestSuite()
suite.addTest(Config('test_config_category'))
runner = AutoTest(suite=suite, name='用例调试', to_user=to_user, case_type='m')
runner.run()
