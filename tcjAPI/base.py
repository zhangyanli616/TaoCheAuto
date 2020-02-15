# -*- coding:utf-8 -*-
import unittest
from titan.tt_log import LOG


class Base(unittest.TestCase):

    def setUp(self):
        LOG.info('【开始】')

    def tearDown(self):
        LOG.info('【结束】')
