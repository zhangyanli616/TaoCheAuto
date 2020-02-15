import unittest
from BeautifulReport import BeautifulReport as bf
from xmdCW.testcase.test_login import TestLogin
from xmdCW.testcase.test_gongzuotai import TestGongDan
from xmdCW.testcase.test_daihezhun import TestDaiHeZhun
from xmdCW.testcase.test_zhunru import TestZhunRu
from xmdCW.testcase.test_wentiFK import TestFanKui
from xmdCW.testcase.test_xianxiaqianyue import TestXianXiaQianYue


if __name__ == "__main__":
    # 定义一个测试集合
    suite = unittest.TestSuite()

    # 把需要执行的用例循环加进来
    for i in (TestGongDan, TestLogin, TestDaiHeZhun, TestZhunRu, TestFanKui, TestXianXiaQianYue):
        suite.addTest(unittest.makeSuite(i))


    # 执行单条用例
    # suite.addTest(unittest.makeSuite(TestLogin))
    run = bf(suite)  # 实例化BeautifulReport模块
    run.report(filename='test', description='车务测试结果')
