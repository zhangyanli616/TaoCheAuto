# -*- coding:utf-8 -*-
from titan import AppiumDriver
import unittest
from taocheApp.config import config
from titan import LOG

appium_service = config.appium_service
desired_caps = config.desired_caps


class Base(unittest.TestCase):
    def setUp(self):
        self.driver = AppiumDriver(appium_service, desired_caps)
        LOG.info("淘车App启动成功")
        self.driver.sleep(1)

    def tearDown(self):
        if self._outcome.errors[1][1]:
            self.driver.screen_shot(self._testMethodName)
