# -*- coding:utf-8 -*-
from titan import SeleniumDriver
from taochePC.config import config
import unittest

is_headless = config.is_headless


class Base(unittest.TestCase):

    def setUp(self):
        # script_path = re.search(r'\\mc\\(.*?).py', os.path.abspath(__file__)).group()
        # LOG.info('【开始】脚本路径:%s' % script_path)
        self.driver = SeleniumDriver(is_headless=is_headless)

    def tearDown(self):
        if self._outcome.errors[1][1]:
            self.driver.screen_shot(self._testMethodName)
        self.driver.close()

