# -*- coding:utf-8 -*-
from titan import SeleniumDriver
from taochePC.config import config
import unittest

is_headless = config.is_headless


class Base(unittest.TestCase):

    def setUp(self):
        mobile_options = "user-agent='Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'"
        self.driver = SeleniumDriver(btype="m", mobile_options=mobile_options)

    def tearDown(self):
        if self._outcome.errors[1][1]:
            self.driver.screen_shot(self._testMethodName)
        self.driver.close()

