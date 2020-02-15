# -*- coding:utf-8 -*-
import requests
from basicAPI.config import config
from titan.tt_log import LOG
from basicAPI.base import Base
from titan import tt_check

active_url = config.active_url

#活动信息接口验证返回结果是否正确

class activeinfo(Base):
    @staticmethod
    def test_activeinfo():
      url1 = 'sales-promotion-platform-externalapi/active/selectByUnifiedNumber?unifiedNumber=020882169'
      response = requests.get(active_url + url1)
      LOG.info("【访问】" + active_url + url1)
      status = response.status_code
      tt_check.assertEqual(status, 200, "请求是否成功：状态码%s" % status)
      tt_check.assertRegex(response.text, "1000元购车券", "返回是否包含成功")

